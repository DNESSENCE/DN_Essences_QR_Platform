import customtkinter as ctk

from config.theme import PRIMARY, CARD
from controllers.settings_controller import SettingsController


class SettingsPage(ctk.CTkFrame):
    """Professional settings and configuration page."""

    def __init__(self, master):
        super().__init__(master, fg_color=PRIMARY)

        self.app_name_entry = None
        self.company_name_entry = None
        self.company_website_entry = None
        self.export_dir_entry = None
        self.db_status_label = None
        self.controller = None

        self.create_layout()

    def create_layout(self) -> None:
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 20))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Settings",
            font=("Segoe UI", 28, "bold"),
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Configure application preferences and database settings",
            font=("Segoe UI", 13),
        )
        subtitle.pack(anchor="w")

        settings_frame = ctk.CTkFrame(self, fg_color="transparent")
        settings_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=(0, 15))
        settings_frame.grid_columnconfigure(0, weight=1)

        self._create_app_settings(settings_frame)
        self._create_database_settings(settings_frame)
        self._create_action_buttons(settings_frame)

        # Controller is created after widgets; callbacks are bound using
        # lambdas so commands resolve at click time and avoid attribute
        # access before initialization.
        self.controller = SettingsController(self)
        # Ensure UI fields are populated after controller initialization
        self.controller.load_settings()

    def _create_app_settings(self, parent) -> None:
        """Create application settings section."""
        section = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )
        section.pack(fill="x", padx=0, pady=(0, 15))
        section.grid_columnconfigure(1, weight=1)

        label = ctk.CTkLabel(
            section,
            text="Application Settings",
            font=("Segoe UI", 16, "bold"),
        )
        label.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(15, 10))

        ctk.CTkLabel(section, text="App Name:").grid(row=1, column=0, sticky="w", padx=20, pady=5)
        self.app_name_entry = ctk.CTkEntry(section)
        self.app_name_entry.grid(row=1, column=1, sticky="ew", padx=20, pady=5)

        ctk.CTkLabel(section, text="Company Name:").grid(row=2, column=0, sticky="w", padx=20, pady=5)
        self.company_name_entry = ctk.CTkEntry(section)
        self.company_name_entry.grid(row=2, column=1, sticky="ew", padx=20, pady=5)

        ctk.CTkLabel(section, text="Company Website:").grid(row=3, column=0, sticky="w", padx=20, pady=5)
        self.company_website_entry = ctk.CTkEntry(section)
        self.company_website_entry.grid(row=3, column=1, sticky="ew", padx=20, pady=5)

        ctk.CTkLabel(section, text="Export Directory:").grid(row=4, column=0, sticky="w", padx=20, pady=5)
        self.export_dir_entry = ctk.CTkEntry(section)
        self.export_dir_entry.grid(row=4, column=1, sticky="ew", padx=20, pady=(5, 15))

    def _create_database_settings(self, parent) -> None:
        """Create database settings section."""
        section = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )
        section.pack(fill="x", padx=0, pady=(0, 15))
        section.grid_columnconfigure(1, weight=1)

        label = ctk.CTkLabel(
            section,
            text="Database Settings",
            font=("Segoe UI", 16, "bold"),
        )
        label.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(15, 10))

        self.db_status_label = ctk.CTkLabel(
            section,
            text="🟡 Loading...",
            font=("Segoe UI", 12),
        )
        self.db_status_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=5)

        test_btn = ctk.CTkButton(
            section,
            text="Test Connection",
            width=140,
            height=32,
        )
        test_btn.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        test_btn.configure(command=lambda: self.controller.test_connection())

        backup_btn = ctk.CTkButton(
            section,
            text="Backup Database",
            width=140,
            height=32,
            fg_color="#16A34A",
            hover_color="#15803D",
        )
        backup_btn.grid(row=2, column=1, sticky="e", padx=20, pady=5)
        backup_btn.configure(command=lambda: self.controller.backup_database())

    def _create_action_buttons(self, parent) -> None:
        """Create action buttons."""
        button_frame = ctk.CTkFrame(parent, fg_color="transparent")
        button_frame.pack(fill="x", padx=0, pady=(0, 15))
        button_frame.grid_columnconfigure(2, weight=1)

        save_btn = ctk.CTkButton(
            button_frame,
            text="Save Settings",
            width=140,
            height=36,
        )
        save_btn.grid(row=0, column=0, sticky="w", padx=0, pady=0)
        save_btn.configure(command=lambda: self.controller.save_settings())

        reset_btn = ctk.CTkButton(
            button_frame,
            text="Reset to Defaults",
            width=140,
            height=36,
            fg_color="#DC2626",
            hover_color="#B91C1C",
        )
        reset_btn.grid(row=0, column=1, sticky="w", padx=10, pady=0)
        reset_btn.configure(command=lambda: self.controller.reset_to_defaults())

        export_btn = ctk.CTkButton(
            button_frame,
            text="Export",
            width=100,
            height=36,
            fg_color="#374151",
            hover_color="#4B5563",
        )
        export_btn.grid(row=0, column=2, sticky="e", padx=(0, 10), pady=0)
        export_btn.configure(command=lambda: self.controller.export_settings())

        import_btn = ctk.CTkButton(
            button_frame,
            text="Import",
            width=100,
            height=36,
            fg_color="#374151",
            hover_color="#4B5563",
        )
        import_btn.grid(row=0, column=3, sticky="e", padx=0, pady=0)
        import_btn.configure(command=lambda: self.controller.import_settings())