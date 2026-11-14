# langchain-practice

Beginner examples for LangChain and retrieval-augmented generation (RAG).

## Trace a LangChain app with LangSmith

`traced_app.py` sends three prompts to OpenAI using LangChain. LangSmith tracing
is enabled through environment variables, so the app itself contains no
LangSmith instrumentation.

Install the required packages:

```powershell
python -m pip install langchain langchain-openai langsmith
```

In PowerShell, set your keys and the project name before running the app:

```powershell
$env:OPENAI_API_KEY = "your-openai-key"
$env:LANGSMITH_TRACING = "true"
$env:LANGSMITH_API_KEY = "your-langsmith-key"
$env:LANGSMITH_PROJECT = "caie-week2"
python traced_app.py
```

The app checks that tracing is enabled and the required variables are present
before making API calls. Then open [LangSmith](https://smith.langchain.com),
select the `caie-week2` project, and inspect the three runs for their prompts,
responses, latency, and token counts. Keep API keys in environment variables;
do not commit them to the repository.
