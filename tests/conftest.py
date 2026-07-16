import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activity_store():
    app_module.reset_activities()
    yield
    app_module.reset_activities()


@pytest.fixture
def client():
    return TestClient(app_module.app)