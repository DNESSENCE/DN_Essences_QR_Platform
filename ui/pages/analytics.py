import customtkinter as ctk

from config.theme import PRIMARY
from controllers.analytics_controller import AnalyticsController
from ui.components.chart_card import ChartCard
from ui.components.analytics_filters import AnalyticsFilters
from ui.components.engagement_card import EngagementCard
from ui.components.performers_table import PerformersTable


class AnalyticsPage(ctk.CTkFrame):
    """Professional analytics and reporting page."""

    def __init__(self, master):
        super().__init__(master, fg_color=PRIMARY)

        self.controller = None
        self.stats_chart = None
        self.distribution_chart = None
        self.engagement_card = None
        self.performers_table = None

        self.create_layout()

    def create_layout(self) -> None:
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 5))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Analytics & Reports",
            font=("Segoe UI", 28, "bold"),
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Track QR code performance and engagement",
            font=("Segoe UI", 13),
        )
        subtitle.pack(anchor="w")

        self.filters = AnalyticsFilters(self)
        self.filters.grid(row=1, column=0, sticky="ew", padx=15, pady=10)

        self.stats_chart = ChartCard(self, title="QR Code Activity")
        self.stats_chart.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 10))

        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.grid(row=3, column=0, sticky="nsew", padx=15, pady=(0, 15))
        bottom_frame.grid_columnconfigure((0, 1), weight=1)
        bottom_frame.grid_rowconfigure(0, weight=1)

        self.engagement_card = EngagementCard(bottom_frame)
        self.engagement_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self.distribution_chart = ChartCard(bottom_frame, title="QR Type Distribution")
        self.distribution_chart.grid(row=0, column=1, sticky="nsew")

        self.performers_table = PerformersTable(self)
        self.performers_table.grid(row=4, column=0, sticky="nsew", padx=15, pady=(0, 15))

        self.controller = AnalyticsController(self)
        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self.filters.set_timeframe_callback(self._on_timeframe_changed)
        self.filters.set_metric_callback(self._on_metric_changed)
        self.filters.set_refresh_callback(self._on_refresh)

    def _on_timeframe_changed(self, timeframe: str) -> None:
        self.controller.set_timeframe(timeframe)

    def _on_metric_changed(self, metric: str) -> None:
        self.controller.set_metric(metric)

    def _on_refresh(self) -> None:
        self.controller.refresh()