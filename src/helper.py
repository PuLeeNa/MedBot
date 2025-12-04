from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os

# Extract data from pdf
def load_pdf(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyMuPDFLoader)
    documents = loader.load()
    return documents

# Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Use HuggingFace Inference API (no model download needed)
def download_hugging_face_embeddings():
    """
    Uses HuggingFace Inference API instead of local model.
    Requires HUGGINGFACE_API_KEY environment variable.
    Get free API key from: https://huggingface.co/settings/tokens
    """
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=os.getenv("HUGGINGFACE_API_KEY"),
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings