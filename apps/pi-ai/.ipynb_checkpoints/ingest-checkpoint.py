import os
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- 1. Build a Robust Path to the Data Directory ---
# Get the absolute path of the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join the script's directory path with the relative path to the data folder
# This creates a reliable path regardless of where you run the script from.
DATA_PATH = os.path.join(script_dir, "data", "converted")

print(f"Looking for documents in: {DATA_PATH}")

# Check if the directory exists before proceeding
if not os.path.exists(DATA_PATH):
    print(f"Error: Directory not found at {DATA_PATH}")
    print("Please make sure the 'data/converted' folder exists and contains your .txt files.")
else:
    # --- 2. Load all TXT Documents from the Directory ---
    loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", show_progress=True)
    documents = loader.load()

    print(f"\nSuccessfully loaded {len(documents)} documents from the directory.")

    # --- 3. Split the Documents into Chunks ---
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    print(f"Split the {len(documents)} documents into {len(chunks)} chunks.")

    # --- 4. Verify the output ---
    if chunks:
        first_chunk = chunks[0]
        source_file = first_chunk.metadata.get('source', 'N/A')
        
        print(f"\n--- Example of the first chunk ---")
        print(f"Source: {os.path.basename(source_file)}") # Print just the filename
        print("Content:")
        print(first_chunk.page_content)
        print("------------------------------------")

        # You can save the chunks or process them further here.
        # For now, we are just printing to confirm it works.
        print("\nData ingestion and chunking complete!")
        
    else:
        print("No chunks were created. Please check if your .txt files have content.")