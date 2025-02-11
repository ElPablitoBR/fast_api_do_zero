from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app  # Ajuste o caminho, caso necessário

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo!"}


def test_mount_report():
    response = client.get("/report")
    # Verifique o status code conforme necessário
    assert response.status_code == HTTPStatus.OK
