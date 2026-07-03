"""MongoDB Atlas connection and database initialization.

This module handles:
- Loading environment variables from .env (dev and packaged builds)
- MongoDB client initialization
- Connection testing
"""

import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv

from config.runtime import get_env_file_path, is_frozen
from utils.message_dialog import (
    show_env_missing_error,
    show_mongodb_uri_missing_error,
    show_mongodb_connection_error,
)


def _initialize_environment():
    """Load environment variables from .env file.

    Handles both development and packaged (PyInstaller) modes.
    Shows user-friendly error dialogs for configuration issues.

    Raises:
        SystemExit: If configuration is invalid (after showing error dialog).
    """
    env_file = get_env_file_path()

    # Check if .env file exists
    if not env_file.exists():
        show_env_missing_error()
        sys.exit(1)

    # Load .env file
    load_dotenv(str(env_file))

    # Verify MONGODB_URI is set
    if not os.getenv("MONGODB_URI"):
        show_mongodb_uri_missing_error()
        sys.exit(1)


# Initialize environment on module load
_initialize_environment()

# Get configuration from environment
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "qr_platform")

# Initialize MongoDB client
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Test connection immediately
    client.admin.command("ping")
    db = client[DATABASE_NAME]
except Exception as error:
    show_mongodb_connection_error(str(error))
    sys.exit(1)


def get_database():
    """Get the MongoDB database instance.

    Returns:
        pymongo.database.Database: The connected database.
    """
    return db


def test_connection():
    """Test MongoDB connection.

    Returns:
        bool: True if connection successful, False otherwise.
    """
    try:
        client.admin.command("ping")
        print("✅ Connected to MongoDB Atlas Successfully!")
        return True
    except Exception as error:
        print(f"❌ Connection Failed: {error}")
        return False