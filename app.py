import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import ollama

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Local AI PDF Chatbot (Ollama + Mistral 7B)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Save uploaded PDF
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load PDF and split into chunks
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Create embeddings and FAISS vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    db = FAISS.from_documents(texts, embeddings)

    # User query
    query = st.text_input("Ask a question about the document")

    if query:
        # Search for relevant chunks
        docs = db.similarity_search(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        # Prepare prompt
        prompt = f"""
You are a helpful assistant reading a document.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

        # Call Ollama local model
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        # Display answer
        st.write(response["message"]["content"])