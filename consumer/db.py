from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def insert_message(data: dict):
    await collection.insert_one(data)

async def get_messages(limit: int = 100, reverse: bool = True):
    sort_order = -1 if reverse else 1
    cursor = collection.find({}, {"_id": 0}).sort("timestamp", sort_order)
    return await cursor.to_list(length=limit)
