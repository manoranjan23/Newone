from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import config
from ..logging import LOGGER  # নিশ্চিত করুন সঠিক ইমপোর্ট হয়েছে

try:
    # MongoDB Async ক্লায়েন্ট
    _mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.get_database("Anon")

    # MongoDB Sync ক্লায়েন্ট
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    pymongodb = _mongo_sync_.get_database("Anon")

    LOGGER.info("Successfully connected to MongoDB.")  # লগ মেসেজ

except Exception as e:
    LOGGER.error(f"Failed to connect to MongoDB: {e}")  # ত্রুটি লগ
    raise