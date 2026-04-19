import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

KNOWLEDGE_DIR = "knowledge_base"
INDEX_FILE = "faiss_index.bin"
DOCS_FILE = "docs.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents():
    docs = []
    for filename in os.listdir(KNOWLEDGE_DIR):
        path = os.path.join(KNOWLEDGE_DIR, filename)
        if os.path.isfile(path) and filename.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    docs.append({
                        "filename": filename,
                        "content": text
                    })
    return docs

def build_index(docs):
    texts = [doc["content"] for doc in docs]
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_FILE)

    with open(DOCS_FILE, "wb") as f:
        pickle.dump(docs, f)

    print("FAISS index created successfully.")

if __name__ == "__main__":
    documents = load_documents()
    build_index(documents)