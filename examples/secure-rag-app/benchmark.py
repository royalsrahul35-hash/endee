import time
from search import search_query

def benchmark():
    start = time.time()
    search_query("AI")
    end = time.time()

    print("Time:", end - start)

if __name__ == "__main__":
    benchmark()
