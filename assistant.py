from typing import Optional

from phi.assistant import Assistant
from phi.knowledge import AssistantKnowledge
from phi.llm.ollama import Ollama
from phi.embedder.ollama import OllamaEmbedder
from phi.vectordb.pgvector import PgVector2
from phi.storage.assistant.postgres import PgAssistantStorage

db_url = "postgresql+psycopg://MACH_3_DB_USERNAME:MACH_3_DB_PASSWORD@mach3db.com"

def get_rag_assistant(
    model: str = "exaone3.5:32b",
    user_id: Optional[str] = None,
    run_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Assistant:
    """Get a mach3db RAG Assistant."""

    embedder = OllamaEmbedder(model=model, dimensions=5120)

    if model == "nomic-embed-text":
        embedder.dimensions = 768

    return Assistant(
        name="mach3db_rag_assistant",
        run_id=run_id,
        user_id=user_id,
        llm=Ollama(model=model),
        storage=PgAssistantStorage(table_name="mach3db_rag_assistant", db_url=db_url),
        knowledge_base=AssistantKnowledge(
            vector_db=PgVector2(
                db_url=db_url,
                collection="mach3db_rag_documents",
                embedder=embedder,
            ),
            # 2 references are added to the prompt
            num_documents=2,
        ),
        # This setting adds references from the knowledge_base to the user prompt
        add_references_to_prompt=True,
        # This setting tells the LLM to format messages in markdown
        markdown=True,
        debug_mode=debug_mode,
        description="You are called 'Mach3Mastermind' and your task is to answer questions from a knowledge base",
        instructions=[
            "When a user asks a question, you will be provided with information from the knowledge base.",
            "Using this information provide a clear and concise answer to the user.",
            "Do not use phrases like 'based on my knowledge' or 'depending on the article'.",
        ],
        add_datetime_to_instructions=True,
    )
