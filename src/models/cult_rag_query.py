from pydantic import BaseModel

class CultQueryInput(BaseModel):
    input: str

class CultQueryOutput(BaseModel):
    message: str
    actions: list