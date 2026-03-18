from sentence_transformers import SentenceTransformer
from data import documents

model = SentenceTransformer("all-MiniLM-L6-v2")
vector_db = []

def ingest_data():
    global vector_db
    embeddings = model.encode(documents)

    for doc, emb in zip(documents, embeddings):
        vector_db.append((doc, emb))
