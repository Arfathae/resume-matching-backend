from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
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

# Create embeddings and nearest neighbors index
embeddings = model.encode([c["profile"] for c in candidates])
nn = NearestNeighbors(n_neighbors=2, metric='cosine')
nn.fit(embeddings)

# Define request format
class Query(BaseModel):
    text: str

# Health check (to see if backend runs)
@app.get("/health")
def health():
    return {"status": "ok"}

# Matching endpoint
@app.post("/match")
def match(query: Query):
    query_vec = model.encode([query.text])
    distances, indices = nn.kneighbors(query_vec)
    results = [candidates[i] for i in indices[0]]
    return {"query": query.text, "matches": results}
