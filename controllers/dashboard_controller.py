from services.dashboard_service import DashboardService


class DashboardController:
    """Controller for dashboard operations."""

    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.service = DashboardService()

    def refresh(self) -> None:
        """Refresh all dashboard data."""
        self.load_statistics()
        self.load_database()
        self.load_activity()

    def load_statistics(self) -> None:
        """Load and display statistics."""
        stats = self.service.get_dashboard_stats()

        self.dashboard.qr_card.set_value(stats["qr_codes"])
        self.dashboard.scan_card.set_value(stats["total_scans"])
        self.dashboard.export_card.set_value(stats.get("total_exports", 0))
        self.dashboard.customer_card.set_value(stats["customers"])
        self.dashboard.product_card.set_value(stats["products"])

    def load_database(self) -> None:
        """Load and display database status."""
        status = self.service.get_database_status()

        self.dashboard.database_card.update_status(status["connected"])
        self.dashboard.database_card.set_database(status["database"])

    def load_activity(self) -> None:
        """Load and display recent activity."""
        activities = self.service.get_recent_activity()

        self.dashboard.activity_table.listbox.delete("1.0", "end")

        for activity in activities:
            self.dashboard.activity_table.listbox.insert("end", "✔ " + activity + "\n")