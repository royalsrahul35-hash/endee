def generate_answer(query, docs):
    context = " ".join(docs)

    return f"""
Context: {context}

Answer:
This is a RAG-based response for: {query}
"""
