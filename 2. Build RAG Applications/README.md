# Build RAG Applications

This directory contains implementations of Retrieval-Augmented Generation (RAG) systems, moving from fundamental LLM interactions and vector indexing to deployment with web interfaces.

* **Key Technologies & Tools:** Python, LangChain, IBM Watsonx AI, ChromaDB, Hugging Face Sentence Transformers (`all-MiniLM-L6-v2`), LlamaIndex, Gradio

---

## 1. Fundamentals of RAG Systems (`rag_intro.ipynb`, `simple_llm.py`, `qabot.py`) 
Covers the core architecture of Retrieval-Augmented Generation, including document processing, vector embeddings, and question-answering capabilities using Watsonx and ChromaDB.

* **LLM Integration:** Direct integration with foundation models (`ibm/granite-13b-chat-v2`) via IBM Watsonx AI API for baseline text generation.
* **Vector Indexing:** Document loading, text splitting, and vector embedding generation using Sentence Transformers (`all-MiniLM-L6-v2`) stored within ChromaDB.
* **Context Retrieval & Generation:** Querying vector stores to retrieve contextually relevant document chunks and passing them as context to the LLM to generate precise, grounded answers.

---

## 2. Context-Aware Applications & Web Interfaces (`Build an AI Icebreaker Bot with LlamaIndex & IBM Granite.md`, `gradio_demo.py`)
Focuses on building domain-specific conversational bots using higher-level orchestration frameworks (LlamaIndex) and deploying them with interactive user interfaces.

* **LlamaIndex Orchestration:** Construction of index-based retrieval pipelines specifically tailored for profile-based persona generation and context retrieval.
* **Interactive UI:** Implementation of web-based user interfaces using Gradio to handle real-time user inputs and display dynamic responses.
* **Granite Model Integration:** Utilization of IBM Granite models within LlamaIndex workflows for localized prompt framing and precise output generation.
