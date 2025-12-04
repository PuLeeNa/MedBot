import warnings
import os
import sys

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
from src.common_responses import check_common_question

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

load_dotenv()

# Lazy initialization of QA chain for Vercel serverless
_qa = None

def get_qa_chain():
    global _qa
    if _qa is None:
        # Initialize embeddings and vector store
        embeddings = download_hugging_face_embeddings()
        index_name = "medical-chatbotn"
        docsearch = PineconeVectorStore.from_existing_index(
            index_name=index_name,
            embedding=embeddings
        )
        
        # Setup LLM and QA chain
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain_type_kwargs = {"prompt": PROMPT}
        
        llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            temperature=0.8,
            max_tokens=1024,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        
        _qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
            return_source_documents=True,
            chain_type_kwargs=chain_type_kwargs
        )
    return _qa

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_msg = msg.strip()
    
    common_response = check_common_question(input_msg)
    if common_response:
        return str(common_response)
    
    qa = get_qa_chain()  # Lazy load QA chain
    result = qa.invoke({"query": input_msg})
    return str(result['result'])
