import os



PROMPTS = [
    "In one sentence, explain what a Python virtual environment is.",
    "Compare LangChain document loaders and text splitters in exactly three concise bullet points.",
    (
        "Explain retrieval-augmented generation (RAG) to a junior developer. "
        "In five numbered steps, describe loading source files, chunking, embedding, "
        "vector search, and generating an answer. Include one practical failure mode "
        "and a concise way to diagnose it. Keep the answer under 180 words."
    ),
]


def validate_environment() -> str:
    required_variables = ("OPENAI_API_KEY", "LANGSMITH_API_KEY", "LANGSMITH_PROJECT")
    missing_variables = [
        name for name in required_variables if not os.environ.get(name, "").strip()
    ]
    if missing_variables:
        raise RuntimeError(
            "Set the following environment variables before running this app: "
            + ", ".join(missing_variables)
        )

    if os.environ.get("LANGSMITH_TRACING", "").strip().lower() != "true":
        raise RuntimeError(
            'LangSmith tracing is not enabled. Set LANGSMITH_TRACING="true" '
            "before running this app."
        )

    return os.environ["LANGSMITH_PROJECT"].strip()


def main() -> None:
    project = validate_environment()
    print(f"Tracing is enabled for LangSmith project: {project}")

    from importlib import import_module

    try:
        ChatOpenAI = import_module("langchain_openai").ChatOpenAI
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependency. Install it with: pip install langchain-openai"
        ) from exc

    llm = ChatOpenAI(model="gpt-4o-mini")
    for index, prompt in enumerate(PROMPTS, start=1):
        response = llm.invoke(prompt)
        print(f"\n--- Run {index} ---")
        print(f"Prompt: {prompt}")
        print(f"Answer: {response.content}")


if __name__ == "__main__":
    main()
