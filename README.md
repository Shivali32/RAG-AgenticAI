# Generative AI, RAG & Agentic Systems

This repository contains practical implementations, standalone scripts, and Jupyter notebooks covering Large Language Model (LLM) application development, Retrieval-Augmented Generation (RAG) architectures, vector database management, Model Context Protocol (MCP) integrations, and stateful multi-agent systems[cite: 1, 2, 4].

---

## Core Technologies & Toolstack

* **Agent Orchestration & Frameworks:** LangChain, LangGraph, LlamaIndex, CrewAI, BeeAI Framework, AG2 (AutoGen), FastMCP[cite: 1, 2, 3]
* **Vector Stores & Indexing:** ChromaDB, FAISS[cite: 3, 11]
* **Foundation Models & APIs:** IBM Watsonx.ai (Granite, Slate, LLaMA), OpenAI (GPT-4o, GPT-4o-mini, DALL-E, Whisper), Anthropic (Claude), Mixtral[cite: 1, 2, 3, 11]
* **Protocols & Standards:** Model Context Protocol (MCP) JSON-RPC 2.0 (STDIO, Streamable HTTP)[cite: 22]
* **Multimodal, Parsing & Media Tools:** Docling, Pydantic, Google Text-to-Speech (gTTS), YouTube Transcript API, PyPDF[cite: 3, 11, 16]
* **Deployment & User Interfaces:** Gradio[cite: 11]

---

## Repository Structure

### 1. Develop GenAI Apps (`/Develop GenAI Apps`)
Focuses on prompt engineering techniques, context framing, in-context learning methods (Zero-Shot, Few-Shot), dynamic prompt templates, and conversational state management using LangChain[cite: 11, 14].

### 2. Build RAG Applications (`/Build RAG Applications`)
Demonstrates core RAG pipeline architectures, document loading, chunking, vector embedding generation, and interactive deployment using Gradio interfaces and IBM Watsonx models[cite: 11, 21].

### 3. Vector Databases & Similarity Search (`/Vector Databases & Similarity Search`)
Covers distance metrics (Cosine Similarity, Euclidean Distance, Dot Product), vector storage setup, metadata-filtered queries, and recommendation systems using ChromaDB and Sentence Transformers[cite: 3, 11].

### 4. Advanced Retrieval & Search Technologies (`/Advanced Retrieval & Search Technologies`)
Explores high-performance vector retrieval techniques using FAISS indexing, advanced LlamaIndex node parsing and retrieval strategies, ensemble retrievers, and specialized RAG applications over external video media[cite: 11, 16, 18].

### 5. Multimodal AI & Application Frameworks (`/Multimodal AI & Application Frameworks`)
Includes applications combining computer vision, speech recognition, speech generation, and image generation using IBM Granite Vision, OpenAI Whisper, DALL-E, and Mixtral[cite: 11].

### 6. Stateful Graphs & Agentic Orchestration (`/Stateful Graphs & Agentic Orchestration`)
Covers dynamic task routing, parallel worker fan-out (`Send`), evaluator-optimizer reflection loops, and persistent session memory checkpointers using LangGraph and LangChain Core[cite: 4, 9].

### 7. Collaborative Multi-Agent Teams & Governance (`/Collaborative Multi-Agent Teams & Governance`)
Demonstrates role-based multi-agent teams with task-centric tool isolation in CrewAI, multi-agent conversational debate with AG2 (AutoGen), and declarative execution guardrails with tool handoffs using the BeeAI framework[cite: 2, 3, 18, 20].

### 8. Model Context Protocol Systems (`/Model Context Protocol Systems`)
Implements end-to-end MCP architectures, including FastMCP server development (tools and resources), stdio/HTTP clients with filesystem roots and sampling callbacks, and multi-server ReAct agent hosts bound to Gradio chat interfaces[cite: 22].
