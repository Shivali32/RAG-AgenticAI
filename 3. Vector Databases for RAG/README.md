# Vector Databases & Similarity Search

This directory focuses on vector embeddings, mathematical similarity measures, and the implementation of vector stores using ChromaDB to perform vector search, metadata filtering, and recommendation generation.

* **Key Technologies & Tools:** Python, NumPy, SciPy, Scikit-learn, ChromaDB, Sentence Transformers (`all-MiniLM-L6-v2`)

---

## 1. Fundamentals of Similarity Search (`Similarity search by hand-v1.ipynb`)
Focuses on manual calculations and low-level implementations of vector distance metrics without external vector database dependencies.

* **Distance Metrics:** Mathematical computation of Cosine Similarity, Euclidean Distance (L2 norm), and Dot Product using NumPy and SciPy.
* **Embedding Evaluation:** Manual vector comparisons and ranking algorithms across structured datasets.

---

## 2. Vector Stores & ChromaDB Operations (`similarity_search.py`, `similarity_employeedata.py`, `books_advanced_search.py`, `Chroma_db-intro.pdf`, `Similarity Search on Text Using a Chroma Vector Database.md`)
Demonstrates how to build, query, and manage persistent vector databases using ChromaDB for semantic search across diverse text datasets.

* **ChromaDB Management:** Creating collections, persisting databases to disk, and defining embedding functions using Sentence Transformers.
* **Metadata Filtering:** Performing complex query filtering using metadata attributes combined with vector similarity search.
* **Dataset Implementations:** Application of semantic search models across diverse domain datasets including book catalogs, HR employee records, and news articles.

---

## 3. Vector-Based Recommendation Systems (`chroma_recommendation_system.pdf`, `chroma_recommendation_system.tar`)
Implements end-to-end item recommendation engines powered by vector embeddings and similarity queries.

* **Recommendation Architecture:** Converting domain-specific items (e.g., movies or products) into vector space to calculate similarity matrices.
* **Nearest-Neighbor Retrieval:** Querying stored embeddings to return top-$k$ contextually and semantically similar items based on user preferences.
