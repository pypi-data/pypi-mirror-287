import warnings
import openai
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import faiss
import pdfplumber
import numpy as np
from docx import Document
import logging
import time
import tiktoken  # For calculating token length
import platform
import zipfile
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub
from odf.opendocument import load
from odf.text import P
import json
import argparse
import importlib.metadata
import diskcache as dc  # Import DiskCache
import markdown2
import subprocess
import webbrowser

# Setup logging
logging.basicConfig(level=logging.INFO)
# Initialize DiskCache
cache = dc.Cache(os.path.join(os.path.expanduser('~'), 'docusearch_cache'))
# Tokenizer to calculate token lengths
tokenizer = tiktoken.get_encoding('cl100k_base')

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module="ebooklib.epub")
warnings.filterwarnings("ignore", category=FutureWarning, module="ebooklib.epub")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
    except pdfplumber.pdfparser.PDFSyntaxError:
        logging.error(f"Error processing PDF file: {pdf_path}. The file is not a valid PDF.")
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return '\n'.join([para.text for para in doc.paragraphs])

# Function to extract text from TXT
def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to extract text from ODT
def extract_text_from_odt(odt_path):
    text = ''
    doc = load(odt_path)
    paragraphs = doc.getElementsByType(P)
    for paragraph in paragraphs:
        for node in paragraph.childNodes:
            if node.nodeType == 3:  # Node.TEXT_NODE
                text += node.data
            elif node.nodeType == 1:  # Node.ELEMENT_NODE
                text += node.firstChild.data if node.firstChild else ''
        text += '\n'
    return text

# Function to extract text from HTML files within a ZIP archive
def extract_text_from_html_zip(zip_path):
    text = ''
    with zipfile.ZipFile(zip_path, 'r') as z:
        for filename in z.namelist():
            if filename.endswith('.html'):
                with z.open(filename) as f:
                    soup = BeautifulSoup(f, 'html.parser')
                    text += soup.get_text() + '\n'
    return text

# Function to extract text from EPUB
def extract_text_from_epub(epub_path):
    text = ''
    book = epub.read_epub(epub_path)
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text += soup.get_text() + '\n'
    return text

# Function to split text into chunks within token limits
def split_text_into_chunks(text, max_tokens):
    tokens = tokenizer.encode(text)
    chunks = []
    while tokens:
        chunk_tokens = tokens[:max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)
        tokens = tokens[max_tokens:]
    return chunks

# Function to generate embeddings using OpenAI
def generate_embeddings(text, api_key, model="text-embedding-ada-002"):
    openai.api_key = api_key
    try:
        chunks = split_text_into_chunks(text, max_tokens=2048)  # Use a smaller chunk size for embeddings
        embeddings = []
        for chunk in chunks:
            response = openai.Embedding.create(
                input=chunk,
                model=model  # Use the appropriate model name
            )
            embeddings.append(response['data'][0]['embedding'])
    except openai.error.AuthenticationError:
        return None
    # Average the embeddings if multiple chunks
    return np.mean(embeddings, axis=0)

# Function to get new files that are not cached
def get_new_files(directory, cached_files):
    current_files = set(os.listdir(directory))
    new_files = current_files - cached_files
    return new_files

# Function to read documents from a directory and generate embeddings
def read_documents(directory, api_key):
    documents, metadatas, ids, embeddings = [], [], [], []
    unsupported_files = []  # Initialize unsupported_files at the start

    if directory in cache:
        logging.info(f"Loading documents from cache for directory: {directory}")
        cached_data = cache[directory]
        cached_files = set(metadata["source"] for metadata in cached_data["metadatas"])
        new_files = get_new_files(directory, cached_files)

        if not new_files:
            return cached_data["documents"], cached_data["metadatas"], cached_data["ids"], cached_data["embeddings"], unsupported_files

        logging.info(f"Processing new files in directory: {directory}")
        documents = cached_data["documents"]
        metadatas = cached_data["metadatas"]
        ids = cached_data["ids"]
        embeddings = list(cached_data["embeddings"])  # Convert to list to append new embeddings
    else:
        logging.info(f"Processing documents in directory: {directory}")
        new_files = set(os.listdir(directory))

    for filename in new_files:
        file_path = os.path.join(directory, filename)
        if filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.lower().endswith(".docx"):
            text = extract_text_from_docx(file_path)
        elif filename.lower().endswith(".txt"):
            text = extract_text_from_txt(file_path)
        elif filename.lower().endswith(".odt"):
            text = extract_text_from_odt(file_path)
        elif filename.lower().endswith(".zip"):
            text = extract_text_from_html_zip(file_path)
        elif filename.lower().endswith(".epub"):
            text = extract_text_from_epub(file_path)
        else:
            unsupported_files.append(filename)
            continue

        if not text:
            logging.warning(f"Skipped empty or invalid file: {file_path}")
            continue

        documents.append(text)
        metadata = {"source": filename}
        metadatas.append(metadata)
        doc_id = os.path.splitext(filename)[0]
        ids.append(doc_id)

        # Generate and store embeddings
        document_embedding = generate_embeddings(text, api_key)
        if document_embedding is None:
            return None, None, None, None, unsupported_files
        embeddings.append(document_embedding)

    # Convert embeddings to a 2D numpy array
    embeddings = np.array(embeddings)

    # Update the cache with new documents
    cache[directory] = {
        "documents": documents,
        "metadatas": metadatas,
        "ids": ids,
        "embeddings": embeddings
    }

    return documents, metadatas, ids, embeddings, unsupported_files

# Function to clear cache
def clear_cache():
    cache.clear()
    logging.info("Cache cleared successfully.")

# Function to split the document into chunks dynamically for querying
def split_document(document, max_tokens=4096):  # Adjust the max_tokens value for queries
    return split_text_into_chunks(document, max_tokens=max_tokens)

# Function to query the OpenAI API for a document chunk
def query_chunk(chunk_num, chunk, question, api_key, model="gpt-4", short_response=False, document_type="default"):
    openai.api_key = api_key
    max_completion_tokens = 512 if not short_response else 128  # Limit the number of tokens for the completion
    max_input_tokens = 8192 - max_completion_tokens  # Ensure the total tokens do not exceed the limit
    chunk = split_text_into_chunks(chunk, max_input_tokens)[0]  # Ensure chunk is within input token limit

    if document_type == "financial":
        prompt = f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a detailed answer in tabular format and cite sentences from the document. Make sure the your response is extremely well structured so I can parse the text, identify potential table structures, and then organize the data into a spreadsheet form"
    else:
        prompt = f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a detailed answer and cite sentences from the document." if not short_response else f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a concise answer and cite sentences from the document."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_completion_tokens  # Ensure the response is within the model's maximum context length
    )
    return chunk_num, response.choices[0].message['content']

# Function to get the answer and citations using parallel processing
def get_answers_with_citations(question, document_chunks, api_key, model="gpt-4", short_response=False, document_type="default"):
    all_evidence = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(query_chunk, i+1, chunk, question, api_key, model, short_response, document_type) for i, chunk in enumerate(document_chunks)]
        for future in as_completed(futures):
            chunk_num, answer = future.result()
            all_evidence.append((chunk_num, answer))
    return all_evidence

# Function to combine answers and citations
def combine_answers_with_citations(evidence_list):
    combined_answer = ""
    citations = []
    for chunk_num, answer in evidence_list:
        combined_answer += f"\n{answer}"
        sentences = [sent.strip() for sent in answer.split('.') if any(word in sent for word in answer.split())]
        citations.extend(sentences)
    return combined_answer, citations

# Function to query FAISS index
def query_index(query_embedding, index, metadatas, documents, embeddings, n_results=1):
    query_embedding = np.array([query_embedding]).astype('float32')  # Ensure it's a 2D array
    distances, indices = index.search(query_embedding, n_results)
    results = []
    for i in range(n_results):
        result = {
            'distance': distances[0][i],
            'metadata': metadatas[indices[0][i]],
            'document': documents[indices[0][i]],
            'embedding': embeddings[indices[0][i]]
        }
        results.append(result)
    return results

# Function to create and add embeddings to a FAISS index based on the dataset size
def create_faiss_index(embeddings, embedding_dim):
    if embeddings.shape[0] < 256:
        # If the dataset is small, use IndexFlatL2
        index = faiss.IndexFlatL2(embedding_dim)
        index.add(embeddings)
    else:
        # If the dataset is large enough, use IndexIVFPQ with dynamic nlist
        nlist = max(1, min(100, embeddings.shape[0] // 4))
        quantizer = faiss.IndexFlatL2(embedding_dim)
        index = faiss.IndexIVFPQ(quantizer, embedding_dim, nlist, 8, 8)  # 8 bytes per vector add option to change as parameter, 8, 16, 32

        # Train the index
        index.train(embeddings)
        # Add embeddings to the index
        index.add(embeddings)

    return index

# Function to normalize folder paths based on the detected operating system
def normalize_folder_path(folder_path):
    user_os = platform.system().lower()
    
    if 'windows' in user_os:
        if folder_path.startswith('/mnt/c'):
            folder_path = folder_path.replace('/mnt/c', 'C:').replace('/', '\\')
    elif 'darwin' in user_os or 'linux' in user_os:
        if folder_path[1] == ':':
            folder_path = folder_path.replace('C:', '/mnt/c').replace('\\', '/')
        else:
            folder_path = folder_path.replace('\\', '/')
    
    return folder_path

# Simplified function to identify relevant chunks with a broad question
def identify_relevant_chunks(query_text, document_chunks, api_key, model="gpt-4"):
    logging.info("Identifying relevant chunks...")
    relevant_chunks = []
    openai.api_key = api_key

    def process_chunk(chunk_num, chunk):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: Does this chunk contain any information relevant to the question: {query_text}?\n\nAnswer 'yes' if this chunk contains relevant information, otherwise answer 'no'. If there is even a single phrase that may be relevant, mark the chunk as 'yes'."}
            ],
            max_tokens=5  # Short response expected
        )
        return chunk_num, response.choices[0].message['content'].strip().lower()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, i+1, chunk) for i, chunk in enumerate(document_chunks)]
        for future in as_completed(futures):
            chunk_num, answer = future.result()
            if answer == "yes":
                relevant_chunks.append((chunk_num, document_chunks[chunk_num - 1]))
                logging.info(f"Chunk {chunk_num} identified as relevant.")
    return relevant_chunks

# Modify process_best_matching_document to include the relevant chunks identification step
def process_best_matching_document(query_text, api_key, folder_path, model="gpt-4", short_response=False, document_type="default"):
    # Detect and normalize folder path based on the operating system
    folder_path = normalize_folder_path(folder_path)

    # Read documents and generate embeddings
    start_time = time.time()
    documents, metadatas, ids, embeddings, unsupported_files = read_documents(folder_path, api_key)
    if documents is None:
        return None, None, unsupported_files
    processing_time = time.time() - start_time
    logging.info(f"Document processing time: {processing_time:.2f} seconds")
    
    embedding_dim = embeddings.shape[1]  # Use shape attribute to get dimension
    embedding_matrix = np.array(embeddings).astype('float32')
    
    # Create a FAISS index
    index = create_faiss_index(embedding_matrix, embedding_dim)
    
    # Generate query embedding
    query_embedding_start_time = time.time()
    query_embedding = generate_embeddings(query_text, api_key)
    query_embedding_time = time.time() - query_embedding_start_time
    if query_embedding is None:
        return None, None, unsupported_files
    logging.info(f"Query embedding generation time: {query_embedding_time:.2f} seconds")
    
    # Query the FAISS index
    results = query_index(query_embedding, index, metadatas, documents, embeddings)
    
    # Get the best matching document details
    best_result = results[0]
    best_document = best_result['document']
    best_metadata = best_result['metadata']['source']

    #filter for relevant chunks
    filter_chunks_start_time = time.time()
    document_chunks = split_document(best_document)
    relevant_chunks = identify_relevant_chunks(query_text, document_chunks, api_key, model)
    filter_chunks_query_time = time.time() - filter_chunks_start_time
    logging.info(f"Filter chunks time: {filter_chunks_query_time:.2f} seconds")
 

    # Get answers and citations using parallel processing on relevant chunks
    gpt_response_start_time = time.time()
    evidence_list = get_answers_with_citations(query_text, [chunk for _, chunk in relevant_chunks], api_key, model, short_response, document_type)
    gpt_response_time = time.time() - gpt_response_start_time
    logging.info(f"GPT response generation time: {gpt_response_time:.2f} seconds")
    
    # Combine answers and extract citations
    answer, citations = combine_answers_with_citations(evidence_list)

    querying_time = time.time() - start_time  # Measure the total time after the query completes
    logging.info(f"Total querying time: {querying_time:.2f} seconds")
    
    return best_metadata, answer, unsupported_files

# Modify process_query to handle the updated process_best_matching_document function
def process_query(query_text, api_key, folder_path, model="gpt-4", short_response=False, document_type="default"):
    if not query_text or not api_key or not folder_path:
        raise ValueError("Query text, API key, and folder path are required")
    
    # Normalize folder path
    folder_path = normalize_folder_path(folder_path)
    
    if not os.path.exists(folder_path):
        logging.error(f"The folder path does not exist: {folder_path}")
        raise FileNotFoundError(f"The folder path does not exist: {folder_path}")
    
    best_metadata, answer, unsupported_files = process_best_matching_document(query_text, api_key, folder_path, model, short_response, document_type)
    
    if best_metadata is None:
        raise ValueError("Invalid API key")
    
    response = {
        "document_source": best_metadata,
        "answer": answer
    }
    
    if unsupported_files:
        response["warning"] = f"The following files are unsupported and were not processed: {', '.join(unsupported_files)}"
    
    document_source = response.get('document_source', 'Unknown Source')
    answer = response.get('answer', 'No answer found')
    warning = response.get('warning', '')

    return document_source, answer, warning

#preview response in browser
def open_in_browser(document, answer, wsl=False):
    
    # Convert Markdown to HTML using markdown2
    html_content = markdown2.markdown(answer, extras=["tables"])

    # Define the output file path
    output_file_path = "output.html"

    # Add CSS styling for better readability
    html_with_style = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Query Result</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f5f5f5;
                margin: 20px;
                line-height: 1.6;
                color: #333;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #0b736e;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #0b736e;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            tr:hover {{
                background-color: #ddd;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
                color: #c7254e;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 4px;
                overflow-x: auto;
                color: #c7254e;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            a {{
                color: #4CAF50;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Document Source: {document}</h1>
            <h2>Answer:</h2>
            {html_content}
        </div>
    </body>
    </html>
    """

    # Save the HTML to a file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(html_with_style)

    # Open the HTML file in the default web browser
    open_file_in_browser(output_file_path, wsl)

    logging.info(f"HTML file created and opened: {output_file_path}")

#Handle opening in browser for any OS
def open_file_in_browser(file_path, wsl=False):
    user_os = platform.system().lower()

    if wsl:
        windows_path = os.path.abspath(file_path).replace('/mnt/c', 'C:').replace('/', '\\')
        subprocess.run(['explorer.exe', windows_path])
        return
    
    if 'windows' in user_os:
        webbrowser.open('file://' + os.path.realpath(file_path))
        
    elif 'darwin' in user_os:  # macOS
        subprocess.run(['open', file_path])
        
    else:  # Linux
        subprocess.run(['xdg-open', file_path])
        
        


def main():
    parser = argparse.ArgumentParser(description='Docusearch Command Line Interface')
    parser.add_argument('--version', action='store_true', help='Show the version of docusearch')
    parser.add_argument('--clear-cache', action='store_true', help='Clear cache of documents')
    args = parser.parse_args()

    if args.version:
        version = importlib.metadata.version('docusearch')
        print(f"Docusearch {version}")

# If you want to use the script from the command line
if __name__ == '__main__':
    main()