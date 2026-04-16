import logging

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse

class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            logging.error(f"Unhandled error: {e}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error"}
            )