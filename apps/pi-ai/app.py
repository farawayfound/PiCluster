import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings # Updated import
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# --- Configuration ---
# Define paths and model names
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db")
EMBEDDING_MODEL_NAME = "qwen3-4b-RAGmodel"
LM_STUDIO_BASE_URL = "http://127.0.0.1:1234"

def main():
    print("--- Initializing Chatbot ---")

    # --- 1. Initialize the Embedding Model ---
    # We use the same model from the ingestion step to ensure consistency.
    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # --- 2. Load the Existing Vector Database ---
    # This loads the database we created in ingest.py from the disk.
    print(f"Loading vector database from: {DB_PATH}")
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3}) # Retrieve top 3 most relevant chunks

    # --- 3. Connect to the Local LLM via LM Studio ---
    # The ChatOpenAI class can be used to connect to any OpenAI API-compatible server.
    print(f"Connecting to LLM at: {LM_STUDIO_BASE_URL}")
    llm = ChatOpenAI(base_url=LM_STUDIO_BASE_URL, api_key="not-required")

    # --- 4. Create the RAG Prompt Template ---
    # This is the most important part for controlling the AI's behavior.
    # We instruct it to ONLY use the provided context and to be honest if it doesn't know.
    template = """
    You are a professional assistant for David Chui. Your task is to answer questions about his skills,
    experience, and projects based ONLY on the following context provided.
    If the context does not contain the answer, you MUST say "I do not have enough information to answer that question."
    Do not make up information. Be concise and professional.

    CONTEXT:
    {context}

    QUESTION:
    {input}

    ANSWER:
    """
    prompt = PromptTemplate.from_template(template)

    # --- 5. Create the RAG Chain ---
    # This chain combines all the elements:
    # 1. Takes the user's question ('input').
    # 2. The 'retriever' gets the relevant documents from the vector DB.
    # 3. The documents and question are formatted by the 'prompt'.
    # 4. The formatted prompt is sent to the 'llm' for a final answer.
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    print("\n--- Chatbot is Ready! ---")
    print("Type 'exit' to quit.")
    
    # --- 6. Start Interactive Chat Loop ---
    while True:
        query = input("\n> ")
        if query.lower() == 'exit':
            break
        
        # Invoke the chain and get the response
        response = rag_chain.invoke({"input": query})
        
        print("\nANSWER:")
        print(response["answer"])

        # (Optional) Uncomment the lines below to see the source documents
        # print("\nSOURCES:")
        # for doc in response["context"]:
        #     print(f"  - {os.path.basename(doc.metadata.get('source', 'N/A'))}")

if __name__ == "__main__":
    main()