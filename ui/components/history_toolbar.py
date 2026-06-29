import customtkinter as ctk
from typing import Callable, Optional

from config.theme import CARD


class HistoryToolbar(ctk.CTkFrame):
    """Toolbar for history page actions."""

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color="#334155",
        )

        self.duplicate_callback = None
        self.delete_callback = None
        self.restore_callback = None
        self.export_callback = None

        self.create_widgets()

    def create_widgets(self) -> None:
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        label = ctk.CTkLabel(
            self,
            text="Actions",
            font=("Segoe UI", 12, "bold"),
        )
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.duplicate_btn = ctk.CTkButton(
            self,
            text="Duplicate",
            width=100,
            height=32,
        )
        self.duplicate_btn.grid(row=0, column=1, padx=5, pady=10)

        self.delete_btn = ctk.CTkButton(
            self,
            text="Delete",
            width=100,
            height=32,
            fg_color="#DC2626",
            hover_color="#B91C1C",
        )
        self.delete_btn.grid(row=0, column=2, padx=5, pady=10)

        self.restore_btn = ctk.CTkButton(
            self,
            text="Restore",
            width=100,
            height=32,
            fg_color="#16A34A",
            hover_color="#15803D",
        )
        self.restore_btn.grid(row=0, column=3, padx=5, pady=10)

        self.export_btn = ctk.CTkButton(
            self,
            text="Export",
            width=100,
            height=32,
        )
        self.export_btn.grid(row=0, column=4, padx=5, pady=10)

        self.refresh_btn = ctk.CTkButton(
            self,
            text="Refresh",
            width=100,
            height=32,
            fg_color="#374151",
            hover_color="#4B5563",
        )
        self.refresh_btn.grid(row=0, column=5, padx=5, pady=10)

    def set_duplicate_callback(self, callback: Callable) -> None:
        self.duplicate_callback = callback
        self.duplicate_btn.configure(command=callback)

    def set_delete_callback(self, callback: Callable) -> None:
        self.delete_callback = callback
        self.delete_btn.configure(command=callback)

    def set_restore_callback(self, callback: Callable) -> None:
        self.restore_callback = callback
        self.restore_btn.configure(command=callback)

    def set_export_callback(self, callback: Callable) -> None:
        self.export_callback = callback
        self.export_btn.configure(command=callback)

    def set_refresh_callback(self, callback: Callable) -> None:
        self.refresh_btn.configure(command=callback)
