from fastapi import FastAPI
from pydantic import BaseModel
from core.core import optimizer
from fastapi.responses import Response

app = FastAPI()

class OptimizeRequest(BaseModel):
    message: str
@app.post("/optimize")

def optimize(prompt: OptimizeRequest):
    result = optimizer(prompt.message)
    return {"": result}






