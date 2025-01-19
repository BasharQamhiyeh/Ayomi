import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch, MagicMock
from app.main import app  # Import your FastAPI app
from app.database.database import db_client
from app.models.database_models import Operation
from app.models.request_models import CalculationRequest
import os
import tempfile

@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
        yield tmp_file.name
    os.unlink(tmp_file.name)


@pytest.mark.asyncio
@patch('app.database.database.db_client.get_operations_collection')
@patch('app.database.database.db_client.insert_operation')
async def test_calculate_valid_input(mock_insert_operation, mock_get_operations_collection, client):
    mock_collection = AsyncMock()
    mock_get_operations_collection.return_value = mock_collection
    mock_insert_operation.return_value = None

    request_payload = {"expression": "3 4 +"}
    response = client.post("/calculate", json=request_payload)

    assert response.status_code == 200
    assert response.json() == {"result": 7}


@pytest.mark.asyncio
@patch('app.database.database.db_client.get_operations_collection')
@patch('app.database.database.db_client.insert_operation')
async def test_calculate_invalid_input(mock_insert_operation, mock_get_operations_collection, client):
    mock_collection = AsyncMock()
    mock_get_operations_collection.return_value = mock_collection
    mock_insert_operation.return_value = None

    request_payload = {"expression": "3 4"}
    response = client.post("/calculate", json=request_payload)

    assert response.status_code == 400
    assert "detail" in response.json()

