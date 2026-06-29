from typing import Any, Dict, List
from datetime import datetime

from services.analytics_service import AnalyticsService


class AnalyticsController:
    """Controller for analytics page operations."""

    def __init__(self, page: Any):
        self.page = page
        self.service = AnalyticsService()
        self.current_timeframe = "monthly"
        self.current_metric = "scans"
        self.refresh()

    def refresh(self) -> None:
        """Refresh all analytics data."""
        self.load_stats()
        self.load_distribution()
        self.load_engagement()
        self.load_top_performers()

    def load_stats(self) -> None:
        """Load time-series statistics based on current timeframe."""
        if self.current_timeframe == "daily":
            data = self.service.get_daily_stats(days=30)
        elif self.current_timeframe == "weekly":
            data = self.service.get_weekly_stats(weeks=12)
        else:
            data = self.service.get_monthly_stats(months=12)

        if hasattr(self.page, "stats_chart"):
            self.page.stats_chart.update_data(data)

    def load_distribution(self) -> None:
        """Load QR type distribution data."""
        data = self.service.get_type_distribution()

        if hasattr(self.page, "distribution_chart"):
            self.page.distribution_chart.update_data(data)

    def load_engagement(self) -> None:
        """Load engagement metrics."""
        metrics = self.service.get_engagement_metrics()

        if hasattr(self.page, "engagement_card"):
            self.page.engagement_card.update_metrics(metrics)

    def load_top_performers(self) -> None:
        """Load top performing QR codes."""
        data = self.service.get_top_performers(metric=self.current_metric, limit=10)

        if hasattr(self.page, "performers_table"):
            self.page.performers_table.update_data(data)

    def set_timeframe(self, timeframe: str) -> None:
        """Set the timeframe for statistics."""
        self.current_timeframe = timeframe
        self.load_stats()

    def set_metric(self, metric: str) -> None:
        """Set the metric for top performers."""
        self.current_metric = metric
        self.load_top_performers()

    def export_report(self, format_type: str) -> None:
        """Export analytics report (future implementation)."""
        pass
