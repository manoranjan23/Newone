from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import config
from ..logging import LOGGER

try:
    # Asynchronous MongoDB client setup
    _mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.get_database("Anon")  # Ensure "Anon" database is fetched correctly

    # Synchronous MongoDB client setup
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    pymongodb = _mongo_sync_.get_database("Anon")  # Ensure "Anon" database is fetched correctly

    LOGGER.info("Successfully connected to MongoDB.")

except Exception as e:
    LOGGER.error(f"Failed to connect to MongoDB: {e}")
    raise