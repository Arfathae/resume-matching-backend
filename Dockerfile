FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080

WORKDIR /app

# System deps for scientific libs and uvloop/httptools
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        ffmpeg \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

# Install deps first for better layer caching
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Cloud Run will send $PORT; expose for documentation
EXPOSE 8080

# Use gunicorn with uvicorn workers; bind to $PORT (env expansion requires shell form)
CMD exec gunicorn app:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT


