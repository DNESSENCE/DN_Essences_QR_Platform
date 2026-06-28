import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in .env")

client = MongoClient(MONGODB_URI)

db = client[DATABASE_NAME]


def get_database():
    return db


def test_connection():
    try:
        client.admin.command("ping")
        print("✅ Connected to MongoDB Atlas Successfully!")
        return True
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return False