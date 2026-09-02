# Generative AI, Advanced RAG & Agentic Systems

This repository contains practical implementations, standalone scripts, and Jupyter notebooks covering Large Language Model (LLM) application development, Retrieval-Augmented Generation (RAG) architectures, vector database management, multi-agent frameworks, Model Context Protocol (MCP) integrations, and an end-to-end Capstone system.

---

## Core Technologies & Toolstack

* **Frameworks & Multi-Agent Orchestration:** LangChain, LangGraph, LlamaIndex, CrewAI, BeeAI Framework, AG2 (AutoGen), FastMCP
* **Vector Databases & Semantic Stores:** ChromaDB, FAISS
* **Foundation Models & Inference APIs:** IBM Watsonx.ai (Granite, Slate, LLaMA), OpenAI API (`gpt-4o`, `gpt-4o-mini`, DALL-E, Whisper), Anthropic (`claude-sonnet-4`), Mixtral
* **Communication Protocols & Interoperability:** Model Context Protocol (MCP) JSON-RPC 2.0 (STDIO, Streamable HTTP)
* **Data Processing, Computer Vision & Audio:** PyPDF, YouTube Transcript API, Google Text-to-Speech (gTTS), Pydantic, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn
* **Deployment & User Interfaces:** Gradio, FastAPI

---

## Repository Structure

### 1. Develop GenAI Apps
Focuses on prompt engineering techniques, context framing, in-context learning patterns (Zero-Shot, One-Shot, Few-Shot), dynamic prompt templates, and conversational state management using LangChain and IBM Watsonx.ai

### 2. Build RAG Applications
Demonstrates core Retrieval-Augmented Generation architectures: document ingestion, tokenization, text chunking, dense vector embeddings, and interactive question-answering deployment using Gradio interfaces.

### 3. Vector Databases for RAG
Covers distance metrics (Cosine Similarity, Euclidean Distance, Dot Product), vector storage initialization, metadata-filtered queries, and recommendation systems using ChromaDB and Sentence Transformers.

### 4. Advanced RAG with VD and Retrievers
Explores high-performance similarity search with FAISS indexing (IVF, Flat, HNSW), advanced LlamaIndex node parsing, and hybrid retrieval systems combining sparse BM25 with dense vector retrievers via `EnsembleRetriever`.

### 5. Build Multimodal Generative AI Applications
Integrates computer vision, speech synthesis, and audio transcription into multimodal RAG pipelines using IBM Granite Vision, LLaMA multimodal variants, OpenAI Whisper, DALL-E, and gTTS.

### 6. Fundamentals of Building AI Agents
Covers foundational function-calling loops, LangChain Expression Language (LCEL) chains, autonomous ReAct loops (`create_openai_tools_agent`, `AgentExecutor`), AST Python REPL sandboxes, and conversational SQL database agents.

### 7. Agentic AI with LangChain and LangGraph
Focuses on stateful, directed graph architectures using LangGraph (`StateGraph`), dynamic routing with conditional edges, evaluator-optimizer reflection loops, parallel worker fan-out (`Send`), and checkpointed memory persistence.

### 8. Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI
Provides a comparative multi-agent study implementing role-based task delegation in CrewAI, conversable multi-agent group chats with AG2 (AutoGen), and requirement-governed execution pipelines with permission gates in the BeeAI Framework.

### 9. Build AI Agents using MCP
Implements client-server architectures under the Model Context Protocol (MCP) using FastMCP: defining tools, resources, and prompt templates, handling STDIO/Streamable HTTP transports, and managing client-side filesystem roots and sampling callbacks.

### 10. Capstone Project
An end-to-end multi-agent and MCP intelligence system featuring automated unstructured data extraction with Pydantic JSON self-repair, an MCP server exposing California culinary datasets, and a full ReAct host agent ("Connoisseur Companion") integrated into a multi-tab Gradio chat application.
