import customtkinter as ctk
from typing import Dict, Any, List

from config.theme import CARD


class ChartCard(ctk.CTkFrame):
    """Generic chart card component for analytics."""

    def __init__(self, master, title: str = "Chart"):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )

        self.title_text = title
        self.chart_data = None
        self.create_widgets()

    def create_widgets(self) -> None:
        title = ctk.CTkLabel(
            self,
            text=self.title_text,
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        self.canvas_frame = ctk.CTkFrame(
            self,
            fg_color="#0F172A",
            corner_radius=10,
        )
        self.canvas_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        placeholder = ctk.CTkLabel(
            self.canvas_frame,
            text="Chart placeholder\n(Integration with charting library)",
            font=("Segoe UI", 13),
            text_color="#64748B",
        )
        placeholder.pack(expand=True, fill="both")

    def update_data(self, data: Dict[str, Any]) -> None:
        """Update chart with new data."""
        self.chart_data = data

    def clear(self) -> None:
        """Clear chart data."""
        self.chart_data = None
