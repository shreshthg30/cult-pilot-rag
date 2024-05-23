from fastapi import FastAPI
from src.agents.cultRagAgent import CultAgentExecutor
from src.models.cult_rag_query import CultQueryInput, CultQueryOutput
from src.utils.async_util import async_retry

app = FastAPI(
    title="Cult Chatbot",
    description="Endpoints for a cult RAG chatbot",
)

@async_retry(max_retries=10, delay=1)
async def invoke_agent_with_retry(query: str):
    """Retry the agent if a tool fails to run.

    This can help when there are intermittent connection issues
    to external APIs.
    """

    cult_agent_executor_instance = CultAgentExecutor().get_executor()

    return await cult_agent_executor_instance.ainvoke({"input": query})

@app.get("/")
async def get_status():
    return {"status": "running"}

@app.post("/cult-rag-agent")
async def query_cult_agent(query: CultQueryInput) -> CultQueryOutput:
    query_response = await invoke_agent_with_retry(query.input)

    return query_response