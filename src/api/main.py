import argparse
from uvicorn import run
from fastapi import FastAPI
from .routes.hello import router as hello_router
from .routes.chat import router as chat_router

app = FastAPI()
app.include_router(hello_router, prefix="/hello")
app.include_router(chat_router, prefix="/chat")

def start(host: str = '127.0.0.1', port: int = 3000, reload: bool = False):
    """Launched with `poetry run start` at root level"""
    run("src.api.main:app", host=host, port=port, reload=reload)

def main():
    parser = argparse.ArgumentParser(description='Start FastAPI server.')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host address to bind the server.')
    parser.add_argument('--port', type=int, default=3000, help='Port number to bind the server.')
    parser.add_argument('--reload', action='store_true', help='Enable auto-reloading.')
    args = parser.parse_args()
    start(host=args.host, port=args.port, reload=args.reload)

if __name__ == "__main__":
    main()
