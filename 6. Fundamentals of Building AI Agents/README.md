# Fundamentals of Building AI Agents

A comprehensive technical repository covering foundational to advanced AI agent development paradigms, including manual tool execution, LangChain Expression Language (LCEL) chains, cyclic ReAct architectures, dynamic structured tool calling, database natural language interfaces, and multi-tool orchestration.

* **Key Technologies & Tools:** Python, LangChain, LangGraph, LangChain Core, LangChain Community, LangChain Experimental, OpenAI API (`gpt-4o-mini`, `gpt-4.1-nano`), IBM Watsonx.ai (`ibm/granite-4-h-small`, `meta-llama/llama-4-maverick-17b-128e-instruct-fp8`), PyTube, yt-dlp, YouTube Transcript API, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, MySQL Connector.

---

## Tool-Calling Mechanics & ReAct Agents (`build_interactive_llm_agents_with_tools.ipynb`, `datawizard_ai_powered_data_analysis.ipynb`)
Demonstrates foundational function-calling execution lifecycles and autonomous ReAct data science workflows.
* **Core Mechanics:** Outlines the complete manual tool execution loop—extracting tool call schemas (`name`, `args`, `id`) from model invocations, routing inputs to functions via lookup maps, wrapping results in `ToolMessage` instances, and generating final grounded answers. Transitions into autonomous agent loops using `create_openai_tools_agent` wrapped by `AgentExecutor` with scratchpad intermediate step handling.
* **Model & Framework Details:** Implemented with LangChain Core, LangChain Community, and OpenAI's `gpt-4o-mini`. Features dataset caching in persistent module-level dictionaries (`DATAFRAME_CACHE`) to eliminate token bloat across multi-turn queries.
* **Application/Interface:** Interactive CLI assistants capable of inspecting directory CSV files, executing dynamic pandas methods via Python's `getattr()`, and training/evaluating scikit-learn models (`RandomForestClassifier`, `RandomForestRegressor`) directly via natural language prompts.

## LCEL Chains & Recursive Tool Calling (`build_a_tool_calling_agent.ipynb`)
Explores fixed-sequence pipelines and dynamic recursive execution architectures for programmatic multimedia retrieval and processing.
* **Core Mechanics:** Implements custom LangChain tools for URL parameter extraction via regular expressions, video subtitle retrieval, search query fetching, metadata parsing, and multi-resolution thumbnail discovery. Compares linear two-step pipelining using `RunnablePassthrough` and `RunnableLambda` against dynamic recursion loops using `RunnableBranch` that repeatedly evaluate and invoke remaining tool calls until completion.
* **Model & Framework Details:** Powered by LangChain, `langchain-openai` (`gpt-4o-mini`), `pytube`, `yt-dlp`, and `youtube-transcript-api`.
* **Application/Interface:** End-to-end command-line processing pipeline generating video summaries, audience analyses, engagement metrics, and visual thumbnail markdown structures.

## Natural Language Data Analytics & Conversational SQL (`create_charts_and_graphs_with_natural_language.ipynb`, `build_an_ai_math_assistant_with_langchain_tool_calling.ipynb`, `Build a Natural Language SQL Agent.pdf`)
Covers conversational agents for statistical plotting, safe code execution, database querying, and multi-tool mathematical computation.
* **Core Mechanics:** Leverages `create_pandas_dataframe_agent` with AST Python REPL sandboxes for automated data transformation and visualization generation. Integrates `create_sql_agent` to inspect database schemas, validate queries using `sql_db_query_checker`, recover from syntax errors, and execute queries across complex relational schemas (joins, grouping, aggregations).
* **Model & Framework Details:** Uses IBM watsonx.ai (`ibm/granite-4-h-small`, `llama-4-maverick-17b-128e-instruct-fp8`), OpenAI models, `SQLDatabase` from LangChain Community with `mysql-connector-python`, Matplotlib, Seaborn, and LangGraph's `create_react_agent`.
* **Application/Interface:** CLI and argument-driven workflows supporting dynamic chart generation (bar charts, box plots, scatter plots, pie charts), multi-step math problem solving with custom power/arithmetic toolkits, and natural language translation against a MySQL database.
