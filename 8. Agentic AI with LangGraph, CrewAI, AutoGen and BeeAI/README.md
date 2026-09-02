# Agentic AI with LangGraph, CrewAI, and BeeAI

This directory contains implementations of agentic architectures, stateful multi-agent workflows, and declarative agent governance across LangGraph, CrewAI, BeeAI Framework, and AG2 (AutoGen)[cite: 2, 3, 4]. Implementations range from graph-based prompt chaining and reflection loops to role-based hierarchical task execution and requirement-constrained tool calling[cite: 2, 4, 9, 20].

* **Key Technologies & Tools:** LangGraph, CrewAI, BeeAI Framework, AG2 (AutoGen), LangChain, LangChain Community, OpenAI API (`gpt-4o`, `gpt-4o-mini`), IBM Watsonx.ai (`meta-llama/llama-4-maverick-17b-128e-instruct-fp8`, `ibm/granite-4-h-small`, `meta-llama/llama-3-3-70b-instruct`), SerperDevTool, PDFSearchTool, ChromaDB, SentenceTransformers[cite: 1, 2, 3, 4, 18, 20].

---

## Graph-Based Orchestration and Iterative Reflection (`Implement Workflow Patterns with LangGraph.ipynb`, `Build LangGraph Design Patterns Orchestration Evaluation.ipynb`)
Focuses on stateful, directed graph architectures using LangGraph to implement prompt chaining, intent-based conditional routing, parallel worker fan-out, and evaluator-optimizer reflection loops[cite: 4, 9].
* **Core Mechanics:** Defines centralized schemas via `TypedDict` (`ChainState`, `RouterState`, `State`) to pass shared context across nodes[cite: 4, 9]. Routing functions dynamically branch flows using `add_conditional_edges()` based on LLM classification or evaluator threshold checks[cite: 4, 9]. Orchestrates dynamic task fan-out using LangGraph's `Send()` API and merges concurrent outputs into shared state via `operator.add` reducers[cite: 9].
* **Model & Framework Details:** Implemented with LangGraph (`StateGraph`, `START`, `END`), LangChain Core, and OpenAI `gpt-4o-mini` with Pydantic structured output validation (`Dishes`, `Feedback`, `Router`)[cite: 4, 9].
* **Application/Interface:** Production-pattern pipelines demonstrating automated job application generation (resume summarization to cover letter drafting), intent classification routing (summarization vs. translation, service dispatch), parallel multilingual translation, and an iterative investment plan generator with risk grading[cite: 4, 9].

## Role-Based Multi-Agent Teams (`CrewAI 101 Building Multi-Agent AI Systems.ipynb`, `Agent-Tool vs Task-Tool in CrewAI.ipynb`, `AG2 101 AutoGen Complete Tutorial.ipynb`)
Demonstrates collaborative multi-agent pipelines leveraging persona specialization, task-level tool isolation, and multi-agent group conversation managers[cite: 3, 18, 20].
* **Core Mechanics:** Configures modular agents with explicit roles, goals, and backstories[cite: 3, 20]. Contrasts agent-centric tool configurations with deterministic task-centric tool bindings (`Task(tools=[...])`) to eliminate model tool-selection overhead and prevent hallucinations[cite: 20]. Uses AG2's `GroupChat` and `GroupChatManager` with turn-based speaker selection methods (`auto`, `round_robin`) and custom termination conditions (`is_termination_msg`)[cite: 18].
* **Model & Framework Details:** Built with CrewAI (`Crew`, `Agent`, `Task`, `Process.sequential`), `crewai-tools` (`SerperDevTool`, `PDFSearchTool`), AG2 (`ConversableAgent`, `AssistantAgent`, `UserProxyAgent`), and models including IBM Watsonx `llama-3-3-70b-instruct`, `granite-4-h-small`, and OpenAI `gpt-4o-mini`[cite: 3, 18, 20].
* **Application/Interface:** End-to-end technical content research and publication pipelines, RAG-enabled customer service FAQ retrieval from local PDF vector stores, interactive code execution environments via `LocalCommandLineCodeExecutor`, and human-in-the-loop bug triage workflows[cite: 3, 18, 20].

## Declarative Agent Governance and Tool Handoffs (`Building Agentic AI Systems with the BeeAI Framework.tar`)
Implements enterprise agent systems using the BeeAI framework, emphasizing deterministic execution rules, security gatekeeping, and inter-agent tool handoffs[cite: 2].
* **Core Mechanics:** Enforces runtime operational boundaries through declarative requirements[cite: 2]. Employs `ConditionalRequirement` to constrain invocation order and frequency (e.g., forcing `ThinkTool` prior to tool usage or limiting maximum tool invocations)[cite: 2]. Integrates `AskPermissionRequirement` to block external tool executions until explicit human-in-the-loop authorization is granted[cite: 2].
* **Model & Framework Details:** Implemented with `beeai_framework` (`RequirementAgent`, `UnconstrainedMemory`), `GlobalTrajectoryMiddleware`, IBM Watsonx (`meta-llama/llama-4-maverick-17b-128e-instruct-fp8`, `ibm/granite-4-h-small`), and native tools (`WikipediaTool`, `OpenMeteoTool`, `ThinkTool`, `HandoffTool`)[cite: 2].
* **Application/Interface:** Controlled multi-agent travel coordination where a primary agent analyzes requirements, requests permission, and delegates sub-queries to destination, weather, and language specialists via encapsulated `HandoffTool` instances[cite: 2].
