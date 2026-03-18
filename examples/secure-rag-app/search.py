import numpy as np
from sentence_transformers import SentenceTransformer
from ingest import vector_db

model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_query(query):
    query_emb = model.encode(query)

    scores = []
    for doc, emb in vector_db:
        score = cosine_similarity(query_emb, emb)
        scores.append((doc, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in scores[:2]]
