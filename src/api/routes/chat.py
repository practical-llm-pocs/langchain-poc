from fastapi import APIRouter
from src.core import agent

router = APIRouter()

@router.post("/agent")
async def post_agent(prompt: str):
    return {"message": agent(prompt)}
