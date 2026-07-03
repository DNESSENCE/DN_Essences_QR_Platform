"""Professional error dialogs for configuration errors.

This module provides functions to display user-friendly error messages
for fatal configuration errors without showing Python tracebacks.
"""

import tkinter as tk
from tkinter import messagebox


def show_configuration_error(title: str, message: str) -> None:
    """Display a professional configuration error dialog.

    Args:
        title: Dialog title.
        message: Error message to display (user-friendly, no traceback).

    Example:
        >>> show_configuration_error(
        ...     "Configuration Error",
        ...     "MongoDB configuration file could not be found.\\n\\n"
        ...     "Please contact the administrator."
        ... )
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.attributes("-topmost", True)  # Bring dialog to front

    messagebox.showerror(title, message)

    root.destroy()


def show_env_missing_error() -> None:
    """Display error dialog when .env file is missing."""
    show_configuration_error(
        "Configuration Error",
        "MongoDB configuration file (.env) could not be found.\n\n"
        "Please ensure the .env file is present in the application directory.\n\n"
        "Contact the administrator if you need assistance.",
    )


def show_mongodb_uri_missing_error() -> None:
    """Display error dialog when MONGODB_URI environment variable is missing."""
    show_configuration_error(
        "Configuration Error",
        "MongoDB connection URI (MONGODB_URI) is not configured.\n\n"
        "Please check your .env file configuration.\n\n"
        "Contact the administrator if you need assistance.",
    )


def show_mongodb_connection_error(error_message: str = None) -> None:
    """Display error dialog when MongoDB connection fails.

    Args:
        error_message: Optional detailed error message.
    """
    message = (
        "Failed to connect to MongoDB Atlas.\n\n"
        "Please check:\n"
        "• Your internet connection\n"
        "• MongoDB Atlas credentials in .env\n"
        "• IP whitelist settings in MongoDB Atlas\n\n"
        "Contact the administrator if you need assistance."
    )

    if error_message:
        message += f"\n\nDetails: {error_message}"

    show_configuration_error("Connection Error", message)
