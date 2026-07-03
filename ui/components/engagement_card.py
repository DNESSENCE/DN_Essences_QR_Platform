import customtkinter as ctk
from typing import Dict, Any

from config.theme import CARD, TEXT_SECONDARY


class EngagementCard(ctk.CTkFrame):
    """Card displaying engagement metrics."""

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )

        self.metrics = {}
        self.create_widgets()

    def create_widgets(self) -> None:
        title = ctk.CTkLabel(
            self,
            text="Engagement Metrics",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        metrics_frame = ctk.CTkFrame(self, fg_color="transparent")
        metrics_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        metrics_frame.grid_columnconfigure((0, 1), weight=1)
        metrics_frame.grid_rowconfigure((0, 1), weight=1)

        self.total_qr_label = self._create_metric_display(
            metrics_frame, "Total QR Codes", "0", 0, 0
        )
        self.avg_scans_label = self._create_metric_display(
            metrics_frame, "Avg Scans/QR", "0", 0, 1
        )
        self.avg_exports_label = self._create_metric_display(
            metrics_frame, "Avg Exports/QR", "0", 1, 0
        )
        self.engagement_label = self._create_metric_display(
            metrics_frame, "Engagement Rate", "0%", 1, 1
        )

    def _create_metric_display(self, parent, label: str, value: str, row: int, col: int):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)

        label_widget = ctk.CTkLabel(
            frame,
            text=label,
            font=("Segoe UI", 11),
            text_color=TEXT_SECONDARY,
        )
        label_widget.grid(row=0, column=0, sticky="w")

        value_label = ctk.CTkLabel(
            frame,
            text=value,
            font=("Segoe UI", 20, "bold"),
        )
        value_label.grid(row=1, column=0, sticky="w")

        return value_label

    def update_metrics(self, metrics: Dict[str, Any]) -> None:
        """Update metrics display."""
        self.metrics = metrics

        self.total_qr_label.configure(text=str(metrics.get("total_qr", 0)))
        self.avg_scans_label.configure(text=str(metrics.get("avg_scans_per_qr", 0)))
        self.avg_exports_label.configure(text=str(metrics.get("avg_exports_per_qr", 0)))
        self.engagement_label.configure(
            text=f"{metrics.get('engagement_rate', 0)}%"
        )
