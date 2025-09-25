import os
import shutil
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
## NEW ## - Import for embeddings and vector store
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

# --- 1. Build a Robust Path to the Data and DB Directories ---
script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(script_dir, "data", "knowledge_base")
DB_PATH = os.path.join(script_dir, "db") # ## NEW ## - Path for the vector database

# --- Main Ingestion Function ---
def main():
    print("--- Starting Data Ingestion and Processing ---")
    
    # Check if the data directory exists
    if not os.path.exists(DATA_PATH):
        print(f"Error: Data directory not found at {DATA_PATH}")
        return

    # ## NEW ## - Clean up old database files if they exist
    if os.path.exists(DB_PATH):
        print(f"Found existing database at {DB_PATH}. Deleting it to create a new one.")
        shutil.rmtree(DB_PATH)

    # --- 2. Load all TXT Documents from the Directory ---
    print(f"\nLoading documents from: {DATA_PATH}")
    loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", show_progress=True)
    documents = loader.load()

    if not documents:
        print("No documents were loaded. Please check the data directory.")
        return
        
    print(f"Successfully loaded {len(documents)} documents.")

    # --- 3. Split the Documents into Chunks ---
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # --- 4. Create Embeddings and Store in ChromaDB ---
    # ## NEW ## - Initialize the embedding model. 
    # 'all-MiniLM-L6-v2' is a good, lightweight model that runs on your CPU.
    print("\nInitializing embedding model...")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # ## NEW ## - Create the vector store from the chunks.
    # This process will take all the text chunks, convert each one into a numerical
    # vector using the embedding model, and store them in the Chroma database.
    # The 'persist_directory' tells Chroma where to save the database files on disk.
    print("Creating and persisting vector store... (This may take a moment)")
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_PATH
    )
    
    print(f"\n--- Ingestion Complete! ---")
    print(f"Vector database has been created and saved to: {DB_PATH}")

# --- Script Execution ---
if __name__ == "__main__":
    main()