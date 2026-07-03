import customtkinter as ctk
from typing import Callable, Optional

from config.theme import CARD, TEXT, TEXT_SECONDARY, ACCENT


class AnalyticsFilters(ctk.CTkFrame):
    """Filter controls for analytics page."""

    TIMEFRAMES = ["Daily", "Weekly", "Monthly"]
    METRICS = ["Scans", "Exports"]

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color="#334155",
        )

        self.timeframe_callback = None
        self.metric_callback = None

        self.create_widgets()

    def create_widgets(self) -> None:
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        ctk.CTkLabel(
            self,
            text="Timeframe",
            font=("Segoe UI", 11, "bold"),
            text_color=TEXT,
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.timeframe_var = ctk.StringVar(value="Monthly")
        self.timeframe_combo = ctk.CTkComboBox(
            self,
            values=self.TIMEFRAMES,
            variable=self.timeframe_var,
            state="readonly",
            width=120,
        )
        self.timeframe_combo.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
        self.timeframe_combo.configure(command=self._on_timeframe_changed)

        ctk.CTkLabel(
            self,
            text="Metric",
            font=("Segoe UI", 11, "bold"),
            text_color=TEXT,
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.metric_var = ctk.StringVar(value="Scans")
        self.metric_combo = ctk.CTkComboBox(
            self,
            values=self.METRICS,
            variable=self.metric_var,
            state="readonly",
            width=120,
        )
        self.metric_combo.grid(row=0, column=3, padx=5, pady=10, sticky="ew")
        self.metric_combo.configure(command=self._on_metric_changed)

        self.refresh_btn = ctk.CTkButton(
            self,
            text="Refresh",
            width=100,
            height=32,
            fg_color=ACCENT,
            hover_color="#15803D",
            text_color=TEXT,
        )
        self.refresh_btn.grid(row=0, column=4, padx=5, pady=10)

    def get_timeframe(self) -> str:
        value = self.timeframe_var.get()
        return value.lower()

    def get_metric(self) -> str:
        value = self.metric_var.get()
        return value.lower()

    def set_timeframe_callback(self, callback: Callable) -> None:
        self.timeframe_callback = callback

    def set_metric_callback(self, callback: Callable) -> None:
        self.metric_callback = callback

    def set_refresh_callback(self, callback: Callable) -> None:
        self.refresh_btn.configure(command=callback)

    def _on_timeframe_changed(self, value: str) -> None:
        if self.timeframe_callback:
            self.timeframe_callback(value.lower())

    def _on_metric_changed(self, value: str) -> None:
        if self.metric_callback:
            self.metric_callback(value.lower())
