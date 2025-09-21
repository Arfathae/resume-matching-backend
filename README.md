# Resume Matching Backend

A FastAPI backend for resume matching using sentence transformers and FAISS for similarity search.

## Setup Instructions

### 1. Activate Virtual Environment

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend

```bash
uvicorn main:app --reload
```

### 4. Test the API

Open your browser and go to: `http://127.0.0.1:8000/docs`

This will show the Swagger UI where you can test the API endpoints.

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /match` - Match resumes based on text query

### Example Usage

Send a POST request to `/match` with JSON body:
```json
{
  "text": "B.Tech student skilled in React"
}
```

## Features

- Uses fine-tuned sentence transformer model for semantic matching
- FAISS for efficient similarity search
- FastAPI with automatic API documentation
- Example candidate profiles for testing
