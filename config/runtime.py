"""Runtime environment detection and path resolution.

This module detects whether the application is running in:
- Development mode (python app.py)
- Packaged mode (PyInstaller EXE)

It provides the correct application root directory for loading configuration files.
"""

import sys
import os
from pathlib import Path


def get_app_root() -> Path:
    """Get the application root directory.

    Returns:
        Path: The root directory of the application.
              - In development: the project root directory
              - In PyInstaller: the temporary extraction directory

    Raises:
        RuntimeError: If running in an unexpected environment.
    """
    # Check if running as PyInstaller EXE
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # Running as PyInstaller executable
        # _MEIPASS contains the temporary extraction directory
        app_root = Path(sys._MEIPASS)
    else:
        # Running in development mode (python app.py)
        # Get the directory of the main script
        app_root = Path(__file__).parent.parent

    return app_root


def get_env_file_path() -> Path:
    """Get the path to the .env file.

    Returns:
        Path: The full path to the .env file.
    """
    app_root = get_app_root()
    env_path = app_root / ".env"
    return env_path


def is_frozen() -> bool:
    """Check if running as a PyInstaller executable.

    Returns:
        bool: True if running as EXE, False if in development.
    """
    return getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")


def is_development() -> bool:
    """Check if running in development mode.

    Returns:
        bool: True if running in development, False if packaged.
    """
    return not is_frozen()
