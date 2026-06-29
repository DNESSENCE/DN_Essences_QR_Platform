from datetime import datetime, timedelta
from typing import Dict, Any, List
from collections import defaultdict

from services.history_service import HistoryService
from models.qr_model import QRModel


class AnalyticsService:
    """Service for QR analytics and reporting."""

    def __init__(self):
        self.history_service = HistoryService()

    def get_daily_stats(self, days: int = 30) -> Dict[str, Any]:
        """Get daily QR statistics for the past N days."""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)

        qr_codes = self.history_service.get_qr_by_date_range(start_date, end_date)

        daily_data = defaultdict(lambda: {"created": 0, "scans": 0, "exports": 0})

        for qr in qr_codes:
            if qr.created_at:
                date_key = qr.created_at.strftime("%Y-%m-%d")
                daily_data[date_key]["created"] += 1
                daily_data[date_key]["scans"] += qr.scan_count
                daily_data[date_key]["exports"] += qr.export_count

        sorted_dates = sorted(daily_data.keys())
        return {
            "labels": sorted_dates,
            "created": [daily_data[d]["created"] for d in sorted_dates],
            "scans": [daily_data[d]["scans"] for d in sorted_dates],
            "exports": [daily_data[d]["exports"] for d in sorted_dates],
        }

    def get_weekly_stats(self, weeks: int = 12) -> Dict[str, Any]:
        """Get weekly QR statistics for the past N weeks."""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(weeks=weeks)

        qr_codes = self.history_service.get_qr_by_date_range(start_date, end_date)

        weekly_data = defaultdict(lambda: {"created": 0, "scans": 0, "exports": 0})

        for qr in qr_codes:
            if qr.created_at:
                week_key = qr.created_at.strftime("W%W-%Y")
                weekly_data[week_key]["created"] += 1
                weekly_data[week_key]["scans"] += qr.scan_count
                weekly_data[week_key]["exports"] += qr.export_count

        sorted_weeks = sorted(weekly_data.keys())
        return {
            "labels": sorted_weeks,
            "created": [weekly_data[w]["created"] for w in sorted_weeks],
            "scans": [weekly_data[w]["scans"] for w in sorted_weeks],
            "exports": [weekly_data[w]["exports"] for w in sorted_weeks],
        }

    def get_monthly_stats(self, months: int = 12) -> Dict[str, Any]:
        """Get monthly QR statistics for the past N months."""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=months * 30)

        qr_codes = self.history_service.get_qr_by_date_range(start_date, end_date)

        monthly_data = defaultdict(lambda: {"created": 0, "scans": 0, "exports": 0})

        for qr in qr_codes:
            if qr.created_at:
                month_key = qr.created_at.strftime("%Y-%m")
                monthly_data[month_key]["created"] += 1
                monthly_data[month_key]["scans"] += qr.scan_count
                monthly_data[month_key]["exports"] += qr.export_count

        sorted_months = sorted(monthly_data.keys())
        return {
            "labels": sorted_months,
            "created": [monthly_data[m]["created"] for m in sorted_months],
            "scans": [monthly_data[m]["scans"] for m in sorted_months],
            "exports": [monthly_data[m]["exports"] for m in sorted_months],
        }

    def get_type_distribution(self) -> Dict[str, Any]:
        """Get QR type distribution."""
        all_qr = self.history_service.get_recent_qr_codes(limit=10000)

        type_counts = defaultdict(int)
        for qr in all_qr:
            type_counts[qr.qr_type] += 1

        labels = list(type_counts.keys())
        values = list(type_counts.values())

        return {
            "labels": labels,
            "values": values,
        }

    def get_engagement_metrics(self) -> Dict[str, Any]:
        """Get engagement metrics (scans vs exports)."""
        stats = self.history_service.get_statistics()

        total_qr = stats.get("total_qr_codes", 1)
        total_scans = stats.get("total_scans", 0)
        total_exports = stats.get("total_exports", 0)

        avg_scans_per_qr = total_scans / total_qr if total_qr > 0 else 0
        avg_exports_per_qr = total_exports / total_qr if total_qr > 0 else 0

        return {
            "total_qr": total_qr,
            "total_scans": total_scans,
            "total_exports": total_exports,
            "avg_scans_per_qr": round(avg_scans_per_qr, 2),
            "avg_exports_per_qr": round(avg_exports_per_qr, 2),
            "engagement_rate": round(
                (total_scans / max(total_qr * 10, 1)) * 100, 2
            ),
        }

    def get_top_performers(self, metric: str = "scans", limit: int = 10) -> List[Dict[str, Any]]:
        """Get top performing QR codes by metric."""
        if metric == "scans":
            qr_list = self.history_service.get_most_scanned_qr(limit=limit)
        elif metric == "exports":
            qr_list = self.history_service.get_most_exported_qr(limit=limit)
        else:
            qr_list = self.history_service.get_recent_qr_codes(limit=limit)

        return [
            {
                "id": str(qr._id)[:8],
                "type": qr.qr_type,
                "value": qr.raw_value[:25] + "..." if len(qr.raw_value) > 25 else qr.raw_value,
                "scans": qr.scan_count,
                "exports": qr.export_count,
                "created_at": qr.created_at.strftime("%Y-%m-%d") if qr.created_at else "N/A",
            }
            for qr in qr_list
        ]
