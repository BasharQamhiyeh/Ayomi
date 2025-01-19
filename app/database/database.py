from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URI
from app.models.database_models import Operation
import logging

logger = logging.getLogger(__name__)

class DatabaseClient:
    def __init__(self, uri: str):
        self.client = AsyncIOMotorClient(uri, maxPoolSize=100)
        self.db = self.client.app_db
        self.operations_collection = self.db.operations
        logger.info("Database client created")

    async def get_operations_collection(self):
        return self.operations_collection

    async def insert_operation(self, operation: Operation):
        try:
            await self.operations_collection.insert_one(operation.__dict__)
        except Exception as e:
            logger.error(f"Error inserting operation: {e}")
            raise


db_client = DatabaseClient(MONGO_URI)
