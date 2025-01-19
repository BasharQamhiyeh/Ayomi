# app/database/database_client.py
from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URI
from app.models.database_models import Operation
from bson import ObjectId

class DatabaseClient:
    def __init__(self, uri: str):
        self.client = AsyncIOMotorClient(uri, maxPoolSize=100)
        self.db = self.client.app_db
        self.operations_collection = self.db.operations

    async def get_operations_collection(self):
        return self.operations_collection

    async def insert_operation(self, operation: Operation):
        # Insert operation object into the database
        await self.operations_collection.insert_one(operation.__dict__)

    async def get_operation_by_id(self, operation_id: str):
        # Fetch operation by ID
        operation = await self.operations_collection.find_one({"_id": ObjectId(operation_id)})
        return operation

# Singleton Database client
db_client = DatabaseClient(MONGO_URI)
