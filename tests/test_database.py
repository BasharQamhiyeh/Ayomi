import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.database_models import Operation

@pytest.fixture
def mock_motor_client():
    mock_client = MagicMock(spec=AsyncIOMotorClient)
    mock_client.app_db = MagicMock()
    mock_client.app_db.operations = AsyncMock()
    return mock_client

@pytest.fixture
def mock_db_client(mock_motor_client):
    with patch("app.database.database.db_client", new_callable=MagicMock) as mock_db_client:
        mock_db_client.client = mock_motor_client
        mock_db_client.operations_collection = mock_motor_client.app_db.operations

        mock_db_client.insert_operation = AsyncMock()
        yield mock_db_client

@pytest.mark.asyncio
async def test_insert_operation(mock_db_client, mock_motor_client):
    mock_collection = AsyncMock()
    mock_motor_client.app_db.operations = mock_collection

    operation = Operation(expression="3 4 +", result=7)
    await mock_db_client.insert_operation(operation)
    mock_db_client.insert_operation.assert_called_once_with(operation)


@pytest.mark.asyncio
async def test_insert_operation(mock_db_client, mock_motor_client):
    mock_collection = AsyncMock()
    mock_motor_client.app_db.operations = mock_collection
    operation = Operation(expression="3 4 +", result=7)

    await mock_db_client.insert_operation(operation)
    mock_db_client.insert_operation.assert_called_once_with(operation)