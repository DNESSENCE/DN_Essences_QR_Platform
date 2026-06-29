from tkinter import messagebox, filedialog
from typing import Any

from services.settings_service import SettingsService


class SettingsController:
    """Controller for settings page operations."""

    def __init__(self, page: Any):
        self.page = page
        self.service = SettingsService()
        self.load_settings()

    def load_settings(self) -> None:
        """Load and display current settings."""
        settings = self.service.get_all_settings()

        if hasattr(self.page, "app_name_entry"):
            self.page.app_name_entry.delete(0, "end")
            self.page.app_name_entry.insert(0, settings.get("app_name", ""))

        if hasattr(self.page, "company_name_entry"):
            self.page.company_name_entry.delete(0, "end")
            self.page.company_name_entry.insert(0, settings.get("company_name", ""))

        if hasattr(self.page, "company_website_entry"):
            self.page.company_website_entry.delete(0, "end")
            self.page.company_website_entry.insert(0, settings.get("company_website", ""))

        if hasattr(self.page, "export_dir_entry"):
            self.page.export_dir_entry.delete(0, "end")
            self.page.export_dir_entry.insert(0, settings.get("export_directory", ""))

        self.update_database_status()

    def update_database_status(self) -> None:
        """Update database connection status."""
        info = self.service.get_database_info()

        if hasattr(self.page, "db_status_label"):
            status_text = (
                f"✅ Connected to {info['database']} ({info['collections']} collections)"
                if info["connected"]
                else "❌ Disconnected"
            )
            self.page.db_status_label.configure(text=status_text)

    def save_settings(self) -> None:
        """Save all settings."""
        try:
            updated_settings = self.service.get_all_settings()

            if hasattr(self.page, "app_name_entry"):
                updated_settings["app_name"] = self.page.app_name_entry.get()

            if hasattr(self.page, "company_name_entry"):
                updated_settings["company_name"] = self.page.company_name_entry.get()

            if hasattr(self.page, "company_website_entry"):
                updated_settings["company_website"] = self.page.company_website_entry.get()

            if hasattr(self.page, "export_dir_entry"):
                updated_settings["export_directory"] = self.page.export_dir_entry.get()

            success, result = self.service.save_settings(updated_settings)

            if success:
                messagebox.showinfo("Success", result)
            else:
                messagebox.showerror("Error", result)
        except Exception as error:
            messagebox.showerror("Error", f"Failed to save settings: {str(error)}")

    def test_connection(self) -> None:
        """Test database connection."""
        success, result = self.service.test_database_connection()

        if success:
            messagebox.showinfo("Connection Test", result)
        else:
            messagebox.showerror("Connection Test", result)

        self.update_database_status()

    def backup_database(self) -> None:
        """Backup database."""
        success, result = self.service.backup_database()

        if success:
            messagebox.showinfo("Backup", result)
        else:
            messagebox.showerror("Backup", result)

    def export_settings(self) -> None:
        """Export settings to file."""
        success, result = self.service.export_settings()

        if success:
            messagebox.showinfo("Export", result)
        else:
            messagebox.showerror("Export", result)

    def import_settings(self) -> None:
        """Import settings from file."""
        filepath = filedialog.askopenfilename(
            title="Import Settings",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )

        if filepath:
            success, result = self.service.import_settings(filepath)

            if success:
                messagebox.showinfo("Import", result)
                self.load_settings()
            else:
                messagebox.showerror("Import", result)

    def reset_to_defaults(self) -> None:
        """Reset all settings to defaults."""
        if messagebox.askyesno("Confirm", "Reset all settings to defaults?"):
            success, result = self.service.reset_to_defaults()

            if success:
                messagebox.showinfo("Reset", result)
                self.load_settings()
            else:
                messagebox.showerror("Reset", result)
