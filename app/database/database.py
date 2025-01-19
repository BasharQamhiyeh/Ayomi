from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI, maxPoolSize=100)  # Manage up to 100 concurrent connections
db = client.app_db
operations_collection = db.operations

async def get_db():
    return db
