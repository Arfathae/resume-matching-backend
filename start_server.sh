#!/bin/bash

# Resume Matching Backend Startup Script

echo "🚀 Starting Resume Matching Backend..."
echo "======================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    echo "Run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import fastapi, uvicorn, sentence_transformers" 2>/dev/null; then
    echo "❌ Dependencies not installed. Installing..."
    pip install -r requirements.txt
fi

# Start the server
echo "🌐 Starting FastAPI server..."
echo "Server will be available at: http://127.0.0.1:8000"
echo "API documentation at: http://127.0.0.1:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn main:app --reload --host 0.0.0.0 --port 8000
