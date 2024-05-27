from fastapi import FastAPI, HTTPException
from src.agents.cultRagAgent import CultAgentExecutor
from fastapi.middleware.cors import CORSMiddleware
from src.models.cult_rag_query import CultQueryInput, CultQueryOutput
from src.utils.async_util import async_retry
from src.apiResponse.actions import apiAction
from src.apiResponse.message import apiMessage

app = FastAPI(
    title="Cult Chatbot",
    description="Endpoints for a cult RAG chatbot",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@async_retry(max_retries=10, delay=1)
async def invoke_agent_with_retry(query: str):
    cult_agent_executor_instance = CultAgentExecutor().get_executor()
    return await cult_agent_executor_instance.ainvoke({"input": query})

@app.get("/healthcheck")
async def get_status():
    return {"status": "running"}

@app.post("/cult-rag-agent", response_model=CultQueryOutput)
async def query_cult_agent(query: CultQueryInput) -> CultQueryOutput:
    try:
        query_response = await invoke_agent_with_retry(query.input)

        query_type = query_response['intermediate_steps'][0][0].__dict__['tool']
        query_response["message"] = apiMessage(query_type, query_response['output'])
        query_response["actions"] = apiAction(query_type)

        return query_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
