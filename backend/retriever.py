import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_FILE = "faiss_index.bin"
DOCS_FILE = "docs.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(INDEX_FILE)

with open(DOCS_FILE, "rb") as f:
    documents = pickle.load(f)

def retrieve_context(query: str, top_k: int = 2):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx]["content"])

    return "\n\n".join(results)