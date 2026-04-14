# app/middlewares/logging_middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import logging
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        logging.info(
            f"{request.method} {request.url.path} "
            f"status={response.status_code} duration={duration:.3f}s"
        )
        return response