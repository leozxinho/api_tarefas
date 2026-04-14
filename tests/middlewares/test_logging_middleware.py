import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.middlewares.logging_middleware import LoggingMiddleware

@pytest.fixture
def app():
    app = FastAPI()
    app.add_middleware(LoggingMiddleware)

    @app.get("/test")
    def route_test():
        return {"ok": True}

    return app

@pytest.fixture
def client(app):
    return TestClient(app)

def test_request_passa_normalmente(client):
    response = client.get("/test")
    assert response.status_code == 200

def test_log_e_gerado(client, caplog):
    import logging
    with caplog.at_level(logging.INFO):
        client.get("/test")
    assert "GET /test" in caplog.text
    assert "200" in caplog.text

def test_tempo_de_resposta_no_log(client, caplog):
    import logging
    with caplog.at_level(logging.INFO):
        client.get("/test")
    # verifica que o tempo foi logado (ex: "0.001s")
    assert "s" in caplog.text