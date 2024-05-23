from pydantic import BaseModel

class CultQueryInput(BaseModel):
    input: str

class CultQueryOutput(BaseModel):
    input: str
    output: str