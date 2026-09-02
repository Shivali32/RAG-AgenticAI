# Multi-Agent Recommendation & MCP Systems

A hands-on implementation guide and repository covering multi-agent recommendation pipelines, interactive Gradio chat assistants, and Model Context Protocol (MCP) integrations using LangChain, LangGraph, and FastMCP.

---

## Hybrid Multi-Agent Recommendation Workflow (`Implement_and_Test_a_Multi_Agent_Recommendation_System.ipynb`)
Designs and runs a multi-agent pipeline coordinating six specialized agents across sequential and parallel stages to generate personalized restaurant and recipe recommendations[cite: 1].

* **Core Architecture:** Implements a 4-phase hybrid architecture operating over a shared `TypedDict` state schema (`INITIAL_STATE`) containing 9 keys (`user_input`, `user_profile`, `retrieved_restaurants`, `retrieved_recipes`, `trend_analysis`, `style_analysis`, `nutrition_analysis`, `final_recommendations`, `workflow_step`)[cite: 1]:
  * **Phase 1: User Analysis (Sequential):** `node_generate_profile` extracts dietary preferences, price sensitivity, and flavor styles[cite: 1].
  * **Phase 2: Candidate Retrieval (Sequential):** `node_retrieve_candidates` retrieves top candidate pools for restaurants and recipes[cite: 1].
  * **Phase 3: Deep Analysis (Parallel):** Uses `concurrent.futures.ThreadPoolExecutor` to execute three specialist nodes concurrently—`node_analyze_trends` (Food Trend Analyst), `node_analyze_styles` (Food Style Expert), and `node_evaluate_nutrition` (Nutrition Expert)—before merging branch results back into state[cite: 1].
  * **Phase 4: Synthesis (Sequential):** `node_generate_recommendations` compiles all analyses into top recommendations accompanied by rationale[cite: 1].
* **Model & Framework Details:** Python 3.12, LangGraph (`langgraph==0.2.0`), LangChain Core (`langchain==0.3.0`), and OpenAI (`gpt-5` / `gpt-4o-mini`)[cite: 1].
* **Application/Interface:** Programmatic execution loop featuring automated validation and quality evaluation routines checking dietary restrictions, cuisine diversity, and candidate counts[cite: 1].

---

## Conversational Intent & Preference Chatbot (`Build_a_Chatbot_Interface_for_the_Recommendation_System.ipynb`)
Wraps recommendation pipelines inside an interactive, conversational Gradio web application with natural language extraction and database tooling[cite: 2].

* **Core Mechanics:** Implements a multi-stage conversational router:
  * **Intent Classification:** `classify_intent` labels incoming queries into 5 categories (`restaurant`, `recipe`, `both`, `clarification`, `database`)[cite: 2].
  * **Preference Extraction:** `extract_preferences` parses natural language prompts into structured JSON preferences (cuisines, dietary needs, occasion, price tier)[cite: 2].
  * **Recommendation Routing:** Directs extracted preferences into recommendation functions and outputs formatted Markdown cards[cite: 2].
* **Model & Framework Details:** Gradio (`gradio==4.29.0`), `langchain-openai` (`gpt-4o-mini`), LangChain Core (`langchain-core==0.2.38`), and FastAPI[cite: 2].
* **Application/Interface:** Multi-tabbed Gradio interface (`gr.Blocks`, `gr.Tabs`) featuring:
  * **Chat Interface:** Chatbot supporting examples, streaming display, and conversational context[cite: 2].
  * **Add Restaurant & Add Recipe Tabs:** Input forms for inserting new restaurant locations and recipe specifications directly into the data layer[cite: 2].
  * **About Tab:** Overview of underlying multi-agent systems and semantic search mechanisms[cite: 2].

---

## Model Context Protocol (MCP) Server, Client & Host Integration (`Build an MCP Server.md`, `Build an MCP Client.md`, `Build a Full MCP Application.md`, `app.py`, `server.py`, `client.py`)
End-to-end implementation of the Model Context Protocol (MCP), standardizing data interfaces, runtime tool discovery, delegated execution, and host interfaces[cite: 4, 5, 6].

* **FastMCP Server (`server.py`):**
  * Exposes static corpora via resources (`culinary-map://california`)[cite: 6, 10].
  * Exposes 3 callable tools: `get_restaurant_info` (structured name lookup), `recommend_by_vibe` (two-pass retrieval over JSON vibe tags and raw text), and `get_review` (qualitative review retrieval)[cite: 6, 10].
* **MCP Client (`client.py`):**
  * Manages asynchronous `ClientSession` streams over standard input/output (`stdio_client`)[cite: 5, 8].
  * Implements **Roots Callbacks** (`list_roots`) to confine server filesystem access to local project scopes[cite: 5, 8].
  * Implements **Sampling Callbacks** (`handle_sampling`), allowing servers to delegate LLM completion requests back to the client using Anthropic's Claude (`claude-sonnet-4-20250514`)[cite: 5, 8].
* **MCP Host Application (`app.py`):**
  * Spawns `server.py` via `PythonStdioTransport`, dynamically discovers tools via `client.list_tools()`, and converts MCP schemas into OpenAI-compatible tool specifications[cite: 4, 7].
  * Binds discovered tools to WatsonX (`ChatWatsonx`, `ibm/granite-4-h-small`) and runs a 10-iteration ReAct loop using `ToolMessage` feedback loops[cite: 4, 7].
  * Deploys a Gradio UI with async generator event handling (`yield`) for dynamic "Thinking..." placeholders and quick-action prompt buttons[cite: 4, 7].
