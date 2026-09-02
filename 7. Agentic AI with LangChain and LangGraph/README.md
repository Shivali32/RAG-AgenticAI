# Agentic AI with LangChain and LangGraph

This directory contains implementations of advanced autonomous agent paradigms using LangGraph, LangChain, and external tool integrations. The modules demonstrate iterative self-critique (Reflection/Reflexion), dynamic reasoning-and-acting loops (ReAct), multi-agent retrieval-augmented generation (DocChat), and stateful graph workflows.

* **Key Technologies & Tools:** LangGraph, LangChain, LangChain Core, LangChain Community, OpenAI API (`gpt-4o-mini`, `gpt-5-nano`), IBM Watsonx.ai (`ibm/granite-4-h-small`, `meta-llama/llama-4-maverick-17b-128e-instruct-fp8`), Tavily Search API, ChromaDB, Docling, BM25, Gradio.

---

## Reflection & Self-Correction Workflows (`Building a Reflection Agent with External Knowledge Integration.ipynb`, `Building a Reflection Agent with LangGraph.ipynb`)
Demonstrates cyclic reflection architectures where an agent generates initial responses, performs rigorous self-critique, fetches external evidence, and revises its output.
* **Core Mechanics:** Employs cyclic directed graphs to manage iterative refinement loops. Prompts force structured outputs via Pydantic schemas (`Reflection`, `AnswerQuestion`, `ReviseAnswer`) separating content, missing details, superfluous data, and search queries. Routing functions enforce iteration thresholds (`MAX_ITERATIONS` or message count checks) before terminating at `END`.
* **Model & Framework Details:** Implemented with LangGraph (`StateGraph`, `MessageGraph`), LangChain Core, Tavily Search API (`TavilySearchResults`), OpenAI models (`gpt-5-nano`, `gpt-4o-mini`), and IBM Watsonx (`ibm/granite-4-h-small`).
* **Application/Interface:** Jupyter Notebook workflow simulating domain-specific critique (e.g., nutritional research and professional content generation), featuring live research query generation and citation-backed revisions.

## Dynamic Reasoning & State Graphs (`ReAct: Build Reasoning and Acting AI Agents with LangGraph.ipynb`, `LangGraph 101: Building Stateful AI Workflows.ipynb`)
Focuses on fundamental and automated ReAct (Reason + Act + Observe) design patterns and stateful graph execution.
* **Core Mechanics:** Implements state machines using `TypedDict` and `add_messages` reducers to maintain conversational context. Models dynamically determine when to trigger tool execution nodes via conditional routing (`should_continue`). Demonstrates authentication state validation, loopbacks on failed credentials, and tool-assisted mathematical and web query operations.
* **Model & Framework Details:** Utilizes LangGraph `StateGraph`, `ChatOpenAI`, IBM Watsonx (`meta-llama/llama-4-maverick-17b-128e-instruct-fp8`), and custom LangChain `@tool` definitions (Tavily search, weather clothing recommender, AST/safe math evaluators).
* **Application/Interface:** Interactive CLI-driven message loops and state-managed conversational interfaces supporting step-by-step diagnostic streaming.

## Multi-Agent Document Retrieval & Verification (`Docchat.pdf`)
A production-grade multi-agent RAG system designed for complex, structured documents containing dense text, tables, and figures.
* **Core Mechanics:** Features a specialized agent pipeline including a Scope/Relevance Checker, a Research Agent, a Verification Agent, and a Self-Correction loop. High-precision extraction is powered by Docling Markdown parsing, while retrieval uses a hybrid ensemble combining BM25 keyword matching and dense vector similarity. If generated answers contain unsupported claims or contradictions, the verification node triggers an automated re-research loop.
* **Model & Framework Details:** Built on LangGraph `StateGraph`, Docling document converter, ChromaDB vector store, IBM Watsonx embeddings (`ibm/slate-125m-english-rtrvr-v2`), and `ibm/granite-4-h-small`.
* **Application/Interface:** A web application powered by Gradio Blocks with session state caching, multi-document upload support, and real-time verification reporting.
