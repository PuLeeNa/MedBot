# 🏥 MedBot

## 🌐 Live Demo

**Try it now:** [https://medic-bot.netlify.app](https://medic-bot.netlify.app)

An intelligent medical chatbot powered by **Groq API (Llama 3.3 70B)**, **LangChain**, and **Pinecone** vector database. This RAG (Retrieval-Augmented Generation) application provides accurate medical information by retrieving relevant context from medical documents and generating fast, high-quality responses using Groq's lightning-fast inference API.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green)
![LangChain](https://img.shields.io/badge/LangChain-1.1.0-orange)

## ✨ Features

- 🤖 **RAG-based Architecture**: Retrieves relevant medical information from documents before generating responses
- ⚡ **Lightning-Fast API**: Powered by Groq's ultra-fast inference (up to 10x faster than local models)
- 🎯 **Vector Search**: Uses Pinecone for efficient semantic search across medical documents
- 💬 **Interactive UI**: Clean, responsive chat interface with typing indicators
- 🆓 **Free Tier Available**: Groq offers generous free API access (14,400 requests/day)
- 🚀 **High-Quality Responses**: Uses Llama 3.3 70B model for superior accuracy
- 📚 **Document Support**: Processes PDF medical documents with PyMuPDF
- 💡 **Smart Caching**: Common responses feature for frequently asked questions

## 🏗️ Architecture

**Split Deployment:**

- **Frontend**: Static files on Netlify
- **Backend**: Flask API on Render (handles AI processing)

This is a **RAG (Retrieval-Augmented Generation)** chatbot:

1. **Retrieval**: Searches Pinecone vector database for relevant medical document chunks
2. **Augmentation**: Injects retrieved context into the prompt template
3. **Generation**: Groq API (Llama 3.3 70B) generates fast, accurate responses based on the context

```
User → Netlify Frontend → Render Backend API → Pinecone → Groq LLM → Response
```

## 🛠️ Tech Stack

### Core Technologies

- **LLM**: Groq API - Llama 3.3 70B Versatile
- **Framework**: LangChain 1.1.0
- **Vector DB**: Pinecone
- **Embeddings**: HuggingFace sentence-transformers (all-MiniLM-L6-v2)
- **Backend**: Flask 3.1.0
- **Model Inference**: langchain-groq 1.1.0

### Key Libraries

- `langchain-groq` - Groq API integration for fast LLM inference
- `langchain-community` - Document loaders and LLM integrations
- `langchain-pinecone` - Pinecone vector store integration
- `langchain-huggingface` - HuggingFace embeddings
- `sentence-transformers` - Text embedding models
- `pymupdf` - PDF document processing
- `python-dotenv` - Environment variable management

## 📦 Prerequisites

- Python 3.10 or higher
- Conda (Anaconda/Miniconda) - Optional
- Pinecone API key ([Get it here](https://www.pinecone.io/))
- Groq API key ([Get free key here](https://console.groq.com/))

## 🚀 Quick Deploy

### Backend (Render)

1. Push to GitHub main branch
2. Auto-deploys via `deploy.yml`
3. Render will auto-detect `render.yaml` configuration

### Frontend (Netlify)

1. Push to GitHub main branch
2. Auto-deploys via Netlify configuration
3. Netlify will auto-detect `netlify.toml` configuration

## 💻 Local Development

### Backend Setup

```bash
cd backend
conda create -n mchatbot python=3.10 -y
conda activate mchatbot
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
python -m http.server 8000
# Visit: http://localhost:8000
```

## ⚙️ Configuration

### Environment Variables

**Backend (.env)**:

```bash
PINECONE_API_KEY=your_pinecone_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**Frontend (app.js)**:

```javascript
const API_URL = "https://your-backend-url.onrender.com";
```

### Get Free API Keys

**Groq API**:

1. Visit [https://console.groq.com/](https://console.groq.com/)
2. Sign up for free account
3. Create API key and copy it

**Pinecone**:

1. Visit [https://www.pinecone.io/](https://www.pinecone.io/)
2. Sign up for free account
3. Create index named "medical-chatbotn"

## 📁 Project Structure

```
MedBot/
│
├── backend/                    # Backend API
│   ├── app.py                  # Flask API server
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Container config
│   ├── data/                   # Medical PDF documents
│   └── src/                    # Source modules
│       ├── __init__.py
│       ├── common_responses.py # Cached responses
│       ├── helper.py           # Utility functions
│       └── prompt.py           # Prompt templates
│
├── frontend/                   # Frontend UI
│   ├── index.html              # Chat interface
│   ├── app.js                  # API client logic
│   ├── style.css               # Styling
│   ├── logo.jpg                # Logo/favicon
│   ├── Dockerfile              # Container config
│   └── netlify.toml            # Netlify config
│
├── .github/workflows/          # CI/CD automation
│   └── deploy.yml              # Deployment workflow
│
├── store_index.py              # Pinecone indexing script
├── setup.py                    # Package setup
├── template.py                 # Project template
├── docker-compose.yaml         # Docker orchestration
└── render.yaml                 # Render config
```

## 🔍 How It Works

### 1. Document Processing (`store_index.py`)

```python
# Load PDFs
documents = load_pdf("data/")

# Split into chunks
text_chunks = text_split(documents)

# Generate embeddings
embeddings = download_hugging_face_embeddings()

# Store in Pinecone
PineconeVectorStore.from_texts(text_chunks, embeddings, index_name="medical-chatbot")
```

### 2. Query Processing (`app.py`)

```python
# User sends query via Flask
query = "What is diabetes?"

# Retrieve relevant context from Pinecone (k=2 chunks)
retriever = docsearch.as_retriever(search_kwargs={'k': 2})

# Generate response using Llama 2 with context
qa = RetrievalQA.from_chain_type(llm, retriever=retriever)
response = qa.invoke({"query": query})
```

### 3. Model Configuration

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Fast and efficient Groq model
    temperature=0.8,                   # Creativity (0=deterministic, 1=creative)
    max_tokens=1024,                   # Maximum response length
    groq_api_key=os.getenv("GROQ_API_KEY")  # API key from .env file
)
```

## 🐛 Troubleshooting

### Issue: Token Limit Exceeded

```
Number of tokens (974) exceeded maximum context length (512)
```

**Solution**: Increase `context_length` and `max_new_tokens` in `app.py`

### Issue: Rate Limit Exceeded

```
Rate limit exceeded: 30 requests per minute
```

**Solutions**:

- Implement request queuing in Flask
- Add caching for common questions (already included)
- Upgrade to Groq paid tier if needed
- Add rate limiting on frontend

### Issue: Invalid API Key

```
AuthenticationError: Invalid API key
```

**Solution**: Verify your Groq API key in `.env` file:

```bash
GROQ_API_KEY=gsk_your_actual_key_here
```

### Issue: Conda Not Recognized

**Solution**: Initialize conda for PowerShell:

```powershell
C:\ProgramData\Anaconda3\Scripts\conda.exe init powershell
```

Then restart PowerShell.

## 🎯 Performance Optimization

### Speed Improvements

Groq API is already optimized for speed (up to 10x faster than local models), but you can further optimize:

1. **Limit Tokens**: Set `max_tokens` to 512 for faster responses
2. **Fewer Retrievals**: Use `search_kwargs={'k': 1}` for single-document retrieval
3. **Use Caching**: Leverage `common_responses.py` for frequent questions
4. **Optimize Embeddings**: Cache embedding results for repeated queries

### Groq Free Tier Limits

- **Requests per minute**: 30 RPM
- **Requests per day**: 14,400 RPD
- **Tokens per minute**: ~20,000 TPM
- **Max context window**: 32,768 tokens

### Rate Limit Management

- Implement request queuing
- Add exponential backoff on rate limit errors
- Cache common responses
- Consider upgrading to paid tier for production

## 🐳 Docker Deployment

### Local Docker Testing

```bash
# Build the Docker image
docker build -t medbot:latest .

# Run with docker-compose
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop containers
docker-compose down
```

### Deploy to Render

1. **Push code to GitHub**:

   ```bash
   git add .
   git commit -m "Add Docker and CI/CD configuration"
   git push origin main
   ```

2. **Set up Render**:

   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect `render.yaml`

3. **Configure Environment Variables** in Render:

   - `PINECONE_API_KEY`: Your Pinecone API key
   - `GROQ_API_KEY`: Your Groq API key

4. **CI/CD is configured** via `.github/workflows/deploy.yml`
   - Automatically deploys on push to main branch
   - Ensure GitHub secrets are configured for your deployment targets

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [Groq](https://groq.com/) - Lightning-fast LLM inference API
- [Meta AI](https://ai.meta.com/) - Llama 3.3 70B model
- [LangChain](https://www.langchain.com/) - RAG framework
- [Pinecone](https://www.pinecone.io/) - Vector database
- [HuggingFace](https://huggingface.co/) - Embeddings models

## 📧 Contact

**PuLeeNa** - [@PuLeeNa](https://github.com/PuLeeNa)

---

⭐ **Star this repository if you find it helpful!**
