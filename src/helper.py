from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

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

# download embeddings model (ultra memory optimized for free tier)
def download_hugging_face_embeddings():
    # Using smaller, lighter model for 512MB RAM constraint
    model_name = "sentence-transformers/paraphrase-MiniLM-L3-v2"  # Smaller than L6
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True, 'batch_size': 1, 'show_progress_bar': False}
    )

    return embeddings