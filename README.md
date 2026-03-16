# Local AI PDF Chatbot

A local AI-powered PDF chatbot built with **Streamlit**, **LangChain**, **FAISS**, and **Ollama/Mistral 7B**. It allows you to upload PDFs and ask questions about their content using local embeddings and a language model.

---

## Features

- Upload PDFs and search their content
- AI answers questions using local vector search (FAISS)
- Fully offline — no API keys required
- Context-aware answers from PDF chunks

---

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/local-ai-pdf-chatbot.git
cd local-ai-pdf-chatbot

Create and activate a Python virtual environment:

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

Install Python dependencies:

pip install streamlit>=1.26 langchain>=0.2 langchain-community>=0.4 langchain-huggingface>=0.2 faiss-cpu ollama python-dotenv requests

Install Ollama (for local AI model): https://ollama.com

Running the App

Start the Streamlit app:

streamlit run app.py

Open the URL printed in your terminal (usually http://localhost:8501)

Upload a PDF

Ask questions about the PDF

The AI will respond using the content of your document

Optional: .gitignore content

Add a .gitignore file in your project folder with:

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/
*.env

# PDFs
temp.pdf
*.pdf

# Streamlit cache
.streamlit/
Notes

Works best with instruction-tuned local models (like Mistral 7B Instruct)

For accurate answers, make sure the relevant context is included in the PDF

Fully local — no cloud API calls required

License

MIT License
```
