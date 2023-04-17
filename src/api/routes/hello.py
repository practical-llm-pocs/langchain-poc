from fastapi import APIRouter
from src.core import hello

router = APIRouter()

@router.get("/{name}")
async def get_hello(name: str):
    return {"message": hello(name)}

@router.get("")
async def get_hello_world():
    return {"message": hello("World")}
