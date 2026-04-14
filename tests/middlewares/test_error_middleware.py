# tests/middlewares/test_error_middleware.py
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.middlewares.error_middleware import ErrorMiddleware

@pytest.fixture
def app():
    app = FastAPI()
    app.add_middleware(ErrorMiddleware)

    @app.get("/ok")
    def route_ok():
        return {"ok": True}

    @app.get("/erro")
    def route_erro():
        raise RuntimeError("erro inesperado")

    return app

@pytest.fixture
def client(app):
    return TestClient(app, raise_server_exceptions=False)

def test_rota_normal_retorna_200(client):
    response = client.get("/ok")
    assert response.status_code == 200

def test_excecao_retorna_500(client):
    response = client.get("/erro")
    assert response.status_code == 500

def test_body_do_erro_padronizado(client):
    response = client.get("/erro")
    assert response.json() == {"detail": "Internal server error"}