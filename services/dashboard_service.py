from datetime import datetime
from typing import Dict, Any, List

from database.mongodb import get_database
from services.history_service import HistoryService


class DashboardService:
    """Service for dashboard statistics and metrics."""

    def __init__(self):
        self.db = get_database()
        self.history_service = HistoryService()

    def get_dashboard_stats(self) -> Dict[str, Any]:
        """Get comprehensive dashboard statistics including QR metrics."""
        stats = {
            "qr_codes": 0,
            "total_scans": 0,
            "total_exports": 0,
            "customers": 0,
            "products": 0,
            "orders": 0,
        }

        try:
            qr_stats = self.history_service.get_statistics()
            stats["qr_codes"] = qr_stats.get("total_qr_codes", 0)
            stats["total_scans"] = qr_stats.get("total_scans", 0)
            stats["total_exports"] = qr_stats.get("total_exports", 0)

            stats["customers"] = self.db["customers"].count_documents({})
            stats["products"] = self.db["products"].count_documents({})
            stats["orders"] = self.db["orders"].count_documents({})
        except Exception:
            pass

        return stats

    def get_database_status(self) -> Dict[str, Any]:
        """Get current MongoDB connection status."""
        try:
            self.db.command("ping")
            return {
                "connected": True,
                "database": self.db.name,
                "collections": len(self.db.list_collection_names()),
            }
        except Exception:
            return {
                "connected": False,
                "database": "Unavailable",
                "collections": 0,
            }

    def get_recent_activity(self) -> List[str]:
        """Get recent activity log entries."""
        try:
            logs = list(
                self.db["audit_logs"].find().sort("_id", -1).limit(10)
            )

            activity = []
            for log in logs:
                activity.append(log.get("message", "Unknown Activity"))

            if len(activity) == 0:
                activity = [
                    "Application Started",
                    "MongoDB Connected",
                    "Dashboard Loaded",
                ]

            return activity
        except Exception:
            return [
                "Application Started",
                "MongoDB Connected",
                "Dashboard Loaded",
            ]

    def get_qr_type_distribution(self) -> List[Dict[str, Any]]:
        """Get QR code type distribution."""
        try:
            return self.history_service.get_most_used_qr_types(limit=5)
        except Exception:
            return []

    def get_top_qr_codes(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get the most scanned or exported QR codes."""
        try:
            top_scanned = self.history_service.get_most_scanned_qr(limit=limit)
            return [
                {
                    "id": str(qr._id)[:8],
                    "type": qr.qr_type,
                    "value": qr.raw_value[:20] + "..." if len(qr.raw_value) > 20 else qr.raw_value,
                    "scans": qr.scan_count,
                    "exports": qr.export_count,
                }
                for qr in top_scanned
            ]
        except Exception:
            return []

    def get_recent_qr_codes(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recently created QR codes."""
        try:
            recent = self.history_service.get_recent_qr_codes(limit=limit)
            return [
                {
                    "id": str(qr._id)[:8],
                    "type": qr.qr_type,
                    "value": qr.raw_value[:20] + "..." if len(qr.raw_value) > 20 else qr.raw_value,
                    "created_at": qr.created_at.strftime("%Y-%m-%d %H:%M:%S") if qr.created_at else "N/A",
                }
                for qr in recent
            ]
        except Exception:
            return []

    def log_activity(self, message: str) -> None:
        """Log an activity to the audit log."""
        try:
            self.db["audit_logs"].insert_one({
                "message": message,
                "timestamp": datetime.utcnow(),
            })
        except Exception:
            pass