import os
from typing import Callable, Any
import asyncio
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import APIKeyHeader

class Backprop:
    def __init__(self):
        self.app = FastAPI()
        self.token = os.getenv("BACKPROP_TOKEN")
        self.api_key_header = APIKeyHeader(name="Authorization", auto_error=False)
        self.model_load_func = None
        self.model_ready = asyncio.Event()
        
        @self.app.on_event("startup")
        async def startup_event():
            if self.model_load_func:
                await self.model_load_func()
            self.model_ready.set()

        @self.app.get("/health")
        async def health_check():
            return {"status": "ok"}

        @self.app.get("/ready")
        async def ready_check():
            if self.model_ready.is_set():
                return {"status": "ready"}
            raise HTTPException(status_code=503, detail="Model not loaded")

    def load_model(self):
        def decorator(func: Callable[[], Any]):
            self.model_load_func = func
            return func
        return decorator

    def endpoint(self, path: str):
        def decorator(func: Callable[[Any], Any]):
            @self.app.post(path)
            async def wrapper(request: Request, api_key: str = Depends(self.api_key_header)):
                if self.token and api_key != f"Bearer {self.token}":
                    raise HTTPException(status_code=403, detail="Could not validate credentials")
                
                await self.model_ready.wait()
                
                body = await request.json()
                result = await func(body)
                return result
            return wrapper
        return decorator

    def get_app(self):
        return self.app
