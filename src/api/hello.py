from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Any, Optional
import sys
import os

# Ensure src is in the path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hello.graph import app as workflow_app

router = APIRouter()

class HelloRequest(BaseModel):
    messages: Optional[List[Any]] = []

@router.post("/hello")
@router.get("/hello")
async def hello_endpoint():
    state = {"messages": []}
    result = workflow_app.invoke(state)
    return JSONResponse(content=result["response"].content)
