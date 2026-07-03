from services.dashboard_service import DashboardService


class DashboardController:
    """Controller for dashboard operations."""

    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.service = DashboardService()
        # Bind quick actions (if the UI provides them)
        try:
            self._bind_quick_actions()
        except Exception:
            # Non-fatal: quick actions are optional
            pass

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

    def _bind_quick_actions(self) -> None:
        """Attach handlers to quick action buttons on the dashboard."""
        qa = getattr(self.dashboard, "quick_action", None)

        if qa is None:
            return

        # Map button label to navigation target or action
        mappings = {
            "➕ Generate QR": "QR Generator",
            "📜 History": "History",
            "👕 Products": "Products",
            "👥 Customers": "Customers",
            "⚙ Settings": "Settings",
        }

        for label, target in mappings.items():
            # bind_action will set the command at pack time
            qa.bind_action(label, lambda t=target: self._navigate(t))

    def _navigate(self, page_name: str) -> None:
        """Navigate the app to a given page name."""
        # The page is placed inside content_frame whose master is the main app
        try:
            app = self.dashboard.master.master
            if hasattr(app, "navigation"):
                app.navigation.show(page_name)
        except Exception:
            return