import pytest
from fastapi.testclient import TestClient
from main import app  # Make sure this points to your FastAPI instance

@pytest.fixture
def client():
    return TestClient(app)
