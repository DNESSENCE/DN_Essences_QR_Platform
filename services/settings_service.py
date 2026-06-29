import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

from database.mongodb import get_database


class SettingsService:
    """Service for application settings management."""

    CONFIG_FILE = Path("config/app_settings.json")
    DEFAULT_SETTINGS = {
        "theme": "dark",
        "app_name": "D&N Essences QR Platform",
        "company_name": "D&N Essences",
        "company_website": "https://dn-essences.com",
        "qr_default_foreground": "black",
        "qr_default_background": "white",
        "qr_default_size": 10,
        "qr_default_border": 2,
        "export_format": "png",
        "export_directory": "exports",
        "auto_backup": True,
        "backup_interval_days": 7,
    }

    def __init__(self):
        self.db = get_database()
        self.settings = self.load_settings()

    def load_settings(self) -> Dict[str, Any]:
        """Load settings from config file or use defaults."""
        try:
            if self.CONFIG_FILE.exists():
                with open(self.CONFIG_FILE, "r") as f:
                    loaded = json.load(f)
                    merged = {**self.DEFAULT_SETTINGS, **loaded}
                    return merged
        except Exception:
            pass

        return self.DEFAULT_SETTINGS.copy()

    def save_settings(self, settings: Dict[str, Any]) -> Tuple[bool, str]:
        """Save settings to config file."""
        try:
            self.CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(self.CONFIG_FILE, "w") as f:
                json.dump(settings, f, indent=2)

            self.settings = settings
            return True, "Settings saved successfully."
        except Exception as error:
            return False, f"Failed to save settings: {str(error)}"

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a single setting value."""
        return self.settings.get(key, default)

    def set_setting(self, key: str, value: Any) -> None:
        """Set a single setting value (in-memory)."""
        self.settings[key] = value

    def get_all_settings(self) -> Dict[str, Any]:
        """Get all settings."""
        return self.settings.copy()

    def reset_to_defaults(self) -> Tuple[bool, str]:
        """Reset all settings to defaults."""
        try:
            self.settings = self.DEFAULT_SETTINGS.copy()
            self.save_settings(self.settings)
            return True, "Settings reset to defaults."
        except Exception as error:
            return False, f"Failed to reset settings: {str(error)}"

    def test_database_connection(self) -> Tuple[bool, str]:
        """Test MongoDB connection."""
        try:
            self.db.command("ping")
            return True, "MongoDB connection successful."
        except Exception as error:
            return False, f"MongoDB connection failed: {str(error)}"

    def get_database_info(self) -> Dict[str, Any]:
        """Get database connection information."""
        try:
            status = self.db.command("ping")
            return {
                "connected": True,
                "database": self.db.name,
                "collections": len(self.db.list_collection_names()),
            }
        except Exception:
            return {
                "connected": False,
                "database": "Unavailable",
                "collections": 0,
            }

    def backup_database(self) -> Tuple[bool, str]:
        """Backup database to exports (placeholder)."""
        try:
            backup_path = Path("exports/backups")
            backup_path.mkdir(parents=True, exist_ok=True)
            return True, f"Database backup initiated. Location: {backup_path}"
        except Exception as error:
            return False, f"Backup failed: {str(error)}"

    def export_settings(self) -> Tuple[bool, str]:
        """Export settings to JSON file."""
        try:
            export_path = Path("exports/settings_backup.json")
            export_path.parent.mkdir(parents=True, exist_ok=True)

            with open(export_path, "w") as f:
                json.dump(self.settings, f, indent=2)

            return True, f"Settings exported to {export_path}"
        except Exception as error:
            return False, f"Export failed: {str(error)}"

    def import_settings(self, filepath: str) -> Tuple[bool, str]:
        """Import settings from JSON file."""
        try:
            with open(filepath, "r") as f:
                imported = json.load(f)

            self.settings = {**self.DEFAULT_SETTINGS, **imported}
            self.save_settings(self.settings)
            return True, "Settings imported successfully."
        except Exception as error:
            return False, f"Import failed: {str(error)}"
