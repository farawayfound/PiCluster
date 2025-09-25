conda create --name rag_chatbot python=3.11 -y
conda activate rag_chatbot

pip install langchain chromadb pypdf sentence-transformers jupyterlab unstructured libmagic

#later after ingest.py runs and finishes in the same directory cd D:\Repos\PiCluster\apps\pi-ai
python ingest.py