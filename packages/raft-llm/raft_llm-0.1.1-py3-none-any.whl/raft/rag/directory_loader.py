from langchain_core.documents import Document
from langchain_text_splitters import RecursiveJsonSplitter
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.html import partition_html
from unstructured.partition.csv import partition_csv
import json
from tqdm import tqdm
from typing import List
import os

CHUNK_SIZE = 1000

def pdf_loader(file_path: str) -> List[Document]:
    # Placeholder function to load PDF files
    elements = partition_pdf(
        filename=file_path, 
        infer_table_structure=True,
        chunking_strategy="by_title",
        max_characters=CHUNK_SIZE,
        )
    documents = [Document(page_content=element.text) for element in elements if element.text]

    return documents

def txt_loader(file_path: str) -> List[Document]:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content into chunks of the specified size
    chunks = [content[i:i+CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]
    documents = [Document(page_content=chunk) for chunk in chunks if chunk.strip()]
    
    return documents

def json_loader(file_path: str) -> List[Document]:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return RecursiveJsonSplitter(max_chunk_size=CHUNK_SIZE).create_documents(data)

def html_loader(file_path: str) -> List[Document]:
    # Load HTML elements using partition_html
    elements = partition_html(
        filename=file_path, 
        infer_table_structure=True,
        max_characters=CHUNK_SIZE,
    )
    
    documents = [Document(page_content=element.text) for element in elements if element.text]

    return documents

def csv_loader(file_path: str) -> List[Document]:
    elements = partition_csv(
        filename=file_path, 
        include_header=True,
        infer_table_structure=True,
    )
    documents = [Document(page_content=element.text) for element in elements if element.text]
    return documents

# Loaders dictionary
loaders = {
    '.pdf': pdf_loader,
    '.txt': txt_loader,
    '.json': json_loader,
    '.html': html_loader,
    '.csv': csv_loader,
}

def load_directory(directory_path: str) -> List[Document]:
    documents = []
    for filename in tqdm(os.listdir(directory_path)):
        file_path = os.path.join(directory_path, filename)
        file_extension = os.path.splitext(filename)[1]
        
        loader = loaders.get(file_extension)
        if loader:
            document = loader(file_path)
            documents.extend(document)
        else:
            print(f"Unsupported file format: {file_extension}")

    print(f"Number of documents loaded: {len(documents)}")
    return documents