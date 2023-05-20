from fastapi.testclient import TestClient
from app.core import config
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": f"This is our secret key: {config.settings.secret_key}"}

