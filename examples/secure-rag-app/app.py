from ingest import ingest_data
from search import search_query
from rag import generate_answer

def main():
    print("🚀 Secure RAG App using Endee")

    while True:
        query = input("\nEnter your question (or 'exit'): ")
        if query.lower() == "exit":
            break

        results = search_query(query)
        answer = generate_answer(query, results)

        print("\n🤖 Answer:\n", answer)

if __name__ == "__main__":
    ingest_data()
    main()
    print("Using vector-based semantic retrieval (Endee-inspired)")
