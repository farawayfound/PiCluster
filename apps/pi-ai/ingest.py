# Import necessary classes from the langchain library
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# --- 1. Define the path to your data ---
# This path now points to the 'converted' folder where all your .txt files are.
# The relative path from the 'notebooks' folder is '../data/converted'.
DATA_PATH = os.path.join('..', 'data', 'knowledge_base')

print(f"Looking for documents in: {os.path.abspath(DATA_PATH)}")

# --- 2. Load all TXT Documents from the Directory ---
# We use DirectoryLoader to load all files from a specific folder.
# The 'glob' argument specifies the pattern to match files. "**/*.txt" means
# look in the current directory and all subdirectories for any file ending with .txt.
loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", show_progress=True)
documents = loader.load()

print(f"Successfully loaded {len(documents)} documents from the directory.")

# --- 3. Split the Documents into Chunks ---
# This process remains the same. The text_splitter takes the list of loaded 
# documents and breaks each one down into smaller, more manageable chunks.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

print(f"Split the {len(documents)} documents into {len(chunks)} chunks.")

# --- 4. Verify the output ---
# Let's print the content and the source of the first chunk to ensure it's working correctly.
if chunks:
    first_chunk = chunks[0]
    source_file = first_chunk.metadata.get('source', 'N/A')
    
    print(f"\n--- Example of the first chunk ---")
    print(f"Source: {source_file}")
    print("Content:")
    print(first_chunk.page_content)
    print("------------------------------------")
else:
    print("No chunks were created. Please check if the directory contains .txt files and the path is correct.")