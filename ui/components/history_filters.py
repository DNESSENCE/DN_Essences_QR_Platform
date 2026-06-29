import customtkinter as ctk
from typing import Callable, Optional
from datetime import datetime, timedelta

from config.theme import CARD


class HistoryFilters(ctk.CTkFrame):
    """Filter panel for history page."""

    QR_TYPES = ["All", "Website", "Instagram", "WhatsApp", "Email", "Phone"]

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color="#334155",
        )

        self.search_callback = None
        self.type_filter_callback = None

        self.create_widgets()

    def create_widgets(self) -> None:
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkLabel(
            self,
            text="Search",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text="Search QR codes...",
            height=32,
        )
        self.search_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self._on_search_changed)

        ctk.CTkLabel(
            self,
            text="Type",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.type_filter = ctk.CTkComboBox(
            self,
            values=self.QR_TYPES,
            state="readonly",
            width=120,
        )
        self.type_filter.grid(row=0, column=3, padx=5, pady=10, sticky="ew")
        self.type_filter.set("All")
        self.type_filter.configure(command=self._on_type_changed)

    def get_search_query(self) -> str:
        return self.search_entry.get().strip()

    def get_filter_type(self) -> str:
        return self.type_filter.get()

    def set_search_callback(self, callback: Callable) -> None:
        self.search_callback = callback

    def set_type_filter_callback(self, callback: Callable) -> None:
        self.type_filter_callback = callback

    def _on_search_changed(self, event) -> None:
        if self.search_callback:
            self.search_callback(self.get_search_query())

    def _on_type_changed(self, value: str) -> None:
        if self.type_filter_callback:
            self.type_filter_callback(value)

    def clear(self) -> None:
        self.search_entry.delete(0, "end")
        self.type_filter.set("All")
