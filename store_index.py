import warnings
import os
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Initializing Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbotn"

# Delete old index if it exists (to recreate with API embeddings)
if index_name in pc.list_indexes().names():
    print(f"Deleting existing index: {index_name}")
    pc.delete_index(index_name)
    print(f"Index {index_name} deleted successfully")
    import time
    time.sleep(10)  # Wait for deletion to complete

# Create new index with API embeddings
print(f"Creating new index: {index_name}")
pc.create_index(
    name=index_name,
    dimension=384,  # all-MiniLM-L6-v2 dimension
    metric='cosine',
    spec=ServerlessSpec(
        cloud='aws',
        region="us-east-1"
    )
)
print("Index created successfully")

# Add embeddings to the new index
print("Adding document embeddings to index...")
docsearch = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks], 
    embeddings, 
    index_name=index_name
)
print(f"Successfully indexed {len(text_chunks)} text chunks")
print("Pinecone index is ready!")
