# # Use official Python runtime as base image
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Set environment variables
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PIP_NO_CACHE_DIR=1 \
#     PIP_DISABLE_PIP_VERSION_CHECK=1 \
#     TRANSFORMERS_CACHE=/tmp \
#     HF_HOME=/tmp \
#     TORCH_HOME=/tmp

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first for better caching
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy application code
# COPY . .

# # Create non-root user for security
# RUN useradd -m -u 1000 appuser && \
#     chown -R appuser:appuser /app

# USER appuser

# # Expose port
# EXPOSE 5000

# # Health check
# HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
#     CMD curl -f http://localhost:5000/ || exit 1

# # Run application with gunicorn for production (optimized for low memory)
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--threads", "2", "--timeout", "300", "--max-requests", "100", "--max-requests-jitter", "10", "--worker-tmp-dir", "/dev/shm", "--access-logfile", "-", "--error-logfile", "-", "app:app"]

# FROM python:3.10-slim

# WORKDIR /app

# # Copy requirements and install dependencies
# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# # Copy application code
# COPY . .

# # Expose port
# EXPOSE 5000

# # Run the application
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "app:app","--bind", "0.0.0.0:$PORT", "--workers", "1", "--timeout", "120"]

