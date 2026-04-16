import logging
import time

from application.controllers import task_controller
from fastapi import FastAPI, Request

from application.middlewares.error_middleware import ErrorMiddleware
from application.middlewares.logging_middleware import LoggingMiddleware

app = FastAPI(
    title="Api de tarefas",
    version="1.0.0",
    description="""
Api para gerenciamento de TAREFAS!

<a href="https://github.com/leozxinho/api_tarefas/blob/main/README.md" target="_blank">
👉 Ver documentação completa (README.md)
</a>
"""
)


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logging.info(f"{request.method} {request.url.path} -  {response.status_code} ({duration:.3f}s)")
    return response
    


app.include_router(task_controller.router)
app.add_middleware(LoggingMiddleware)
app.add_middleware(ErrorMiddleware)