from fastapi import APIRouter
from pydantic import BaseModel
from src.core import llama

router = APIRouter()

class ChatRequestDto(BaseModel):
    prompt: str

# POST route with JSON param "prompt" from POST body
@router.post("")
async def agent(req_body: ChatRequestDto):
    return {"message": llama(req_body.prompt)}
