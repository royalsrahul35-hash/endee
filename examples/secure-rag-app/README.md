# 🔐 Secure RAG Application using Endee Vector Database

<h3 align="center">⚡ Semantic Search • 🔐 Queryable Encryption • 🤖 RAG Pipeline</h3>

<p align="center">
A scalable AI system demonstrating fast and secure vector search inspired by Endee.
</p>

---

## 📌 Project Overview

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system built using a vector database approach inspired by Endee.

The system retrieves relevant information from stored data using **semantic search** and generates meaningful responses. It also includes a basic encryption module to simulate secure data handling.

🔐 Queryable Encryption

This project demonstrates a basic simulation of queryable encryption.

- Data is encrypted before storage
- Queries are processed without exposing raw data
- Ensures privacy-preserving search

This aligns with Endee’s vision of secure and efficient vector search.

💡 Why Endee?

Endee is designed for:
- High-performance vector search
- Low-latency retrieval
- Secure queryable encryption

This project demonstrates how such a system can be used
to build scalable and secure AI applications.

---

## 🚀 Features

* 🔍 Semantic Search using vector similarity
* 🤖 RAG-based response generation
* 🔐 Data encryption simulation
* 📊 Performance benchmarking
* 🧩 Modular code structure

---

## 🏗 System Architecture

User Query
↓
Search Module (Semantic Search)
↓
Retrieve Relevant Documents
↓
RAG Module (Generate Answer)
↓
Final Response

---

## 🔄 Workflow

1. Data is stored as documents in the system
2. Documents are converted into embeddings (vector format)
3. User inputs a query
4. Query is converted into vector representation
5. Similar documents are retrieved using semantic search
6. Retrieved data is passed to the RAG module
7. Final response is generated

---

## 📁 Project Structure

```
examples/secure-rag-app/
│── app.py            # Main application entry point
│── data.py           # Sample dataset
│── ingest.py         # Data ingestion logic
│── search.py         # Semantic search module
│── rag.py            # Response generation logic
│── encryption.py     # Data encryption simulation
│── benchmark.py      # Performance testing
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee/examples/secure-rag-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
python app.py
```

---

## 💡 Example Usage

**Input:**

```
What is Artificial Intelligence?
```

**Output:**

```
Artificial Intelligence is transforming the world by enabling machines to learn and make decisions.
```

---

## 📊 Benchmarking

Run performance testing using:

```bash
python benchmark.py
```

---

## 🔐 Use of Endee

This project is built as part of the Endee evaluation process and follows a **vector database-based architecture** inspired by Endee.

* Demonstrates how vector search enables semantic understanding
* Shows how RAG systems retrieve and generate responses
* Simulates secure data handling using encryption

---

## 🚧 Future Improvements

* Integration with real embedding models (OpenAI, Sentence Transformers)
* Use of actual Endee vector database APIs
* Web-based UI using Flask/Streamlit
* Advanced query understanding

---

## 🎥 Demo

(Add your demo video link here)

---

## 📌 Submission

This project is submitted as part of the Endee hiring evaluation.

---
