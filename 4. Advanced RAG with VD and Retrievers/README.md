# Advanced Retrieval & Search Technologies

This directory contains implementations of vector search engines, advanced retrieval techniques using LangChain and LlamaIndex, and custom retrieval applications over external video media.

* **Key Technologies & Tools:** Python, FAISS, LangChain, LlamaIndex, IBM Watsonx AI, YouTube Transcript API, PyPDF

---

## 1. High-Performance Vector Indexing (`Semantic Similarity with FAISS.ipynb`)
Focuses on efficient similarity search over dense vectors using Facebook AI Similarity Search (FAISS).

* **Index Construction:** Building flat and quantized FAISS vector indices for fast nearest-neighbor retrieval.
* **Vector Operations:** Converting text documents into embeddings and executing high-speed similarity queries across large vector spaces.

---

## 2. Framework-Driven Retrieval Pipelines (`Build a Smarter Search with LangChain Context Retrieval.ipynb`, `Explore Advanced Retrievers in LlamaIndex.ipynb`)
Demonstrates advanced search and document retrieval architectures using LangChain and LlamaIndex.

* **LangChain Context Retrieval:** Implementing contextual retrieval chains to optimize document chunking, dynamic context selection, and LLM prompt grounding.
* **LlamaIndex Advanced Retrievers:** Building hierarchical node parsing, vector store index querying, and retriever optimizations for targeted information extraction.

---

## 3. Media-Based Retrieval Applications (`ytbot.py`, `ybot.pdf`)
Implements an end-to-end retrieval tool to extract, process, and query transcripts from external video sources.

* **Transcript Ingestion:** Fetching and parsing transcripts automatically using the YouTube Transcript API.
* **Q&A System:** Chunking transcript data, embedding context into a vector index, and querying the model for interactive video question-answering.
