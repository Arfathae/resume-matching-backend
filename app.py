from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize FastAPI app
app = FastAPI(title="Resume Matcher API")

# Load your fine-tuned model (replace with your model name if different)
model = SentenceTransformer("Arfathkael/fine-tuned-mpnet-triplet")

# Example candidate profiles
candidates = [
    {"id": 1, "profile": "B.Tech with React and Node.js"},
    {"id": 2, "profile": "B.Tech with Python and TensorFlow"},
    {"id": 3, "profile": "B.Des with Figma and UI/UX"},
]

# Create FAISS index
embeddings = model.encode([c["profile"] for c in candidates])
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings).astype(np.float32))

# Define request format
class Query(BaseModel):
    text: str

# Root route for basic availability checks
@app.get("/")
def root():
    return {"message": "Backend is running ✅"}

# Health check (to see if backend runs)
@app.get("/health")
def health():
    return {"status": "ok"}

# Matching endpoint
@app.post("/match")
def match(query: Query):
    query_vec = model.encode([query.text]).astype(np.float32)
    distances, indices = index.search(query_vec, k=2)  # top 2 matches
    results = [candidates[i] for i in indices[0]]
    return {"query": query.text, "matches": results}
