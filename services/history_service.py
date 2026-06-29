from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta

from services.qr_storage_service import QRStorageService
from models.qr_model import QRModel


class HistoryService:
    """Service for managing QR code history and operations."""

    def __init__(self):
        self.storage = QRStorageService()

    def get_recent_qr_codes(self, limit: int = 50) -> List[QRModel]:
        """Get recently created QR codes."""
        return self.storage.get_all_qr(limit=limit)

    def get_qr_by_date_range(self, start_date: datetime, end_date: datetime) -> List[QRModel]:
        """Get QR codes created within a date range."""
        all_qr = self.storage.get_all_qr(limit=1000)
        return [
            qr for qr in all_qr
            if start_date <= qr.created_at <= end_date
        ]

    def get_qr_by_type_and_date(self, qr_type: str, start_date: datetime, end_date: datetime) -> List[QRModel]:
        """Get QR codes filtered by type and date range."""
        all_qr = self.storage.get_qr_by_type(qr_type, limit=1000)
        return [
            qr for qr in all_qr
            if start_date <= qr.created_at <= end_date
        ]

    def duplicate_qr(self, qr_id: str) -> tuple[bool, str]:
        """Create a duplicate of an existing QR code."""
        try:
            original_qr = self.storage.get_qr(qr_id)
            if not original_qr:
                return False, "QR code not found."

            new_qr = QRModel(
                qr_type=original_qr.qr_type,
                raw_value=original_qr.raw_value,
                formatted_value=original_qr.formatted_value,
                foreground_color=original_qr.foreground_color,
                background_color=original_qr.background_color,
                border=original_qr.border,
                size=original_qr.size,
            )
            new_qr.notes = f"Duplicated from {qr_id}"

            success, result = self.storage.save_qr(new_qr)
            if success:
                return True, result
            return False, result
        except Exception as error:
            return False, str(error)

    def restore_deleted_qr(self, qr_id: str) -> tuple[bool, str]:
        """Restore a soft-deleted QR code."""
        try:
            success, result = self.storage.update_qr(
                qr_id,
                {"status": "active"}
            )
            return success, result
        except Exception as error:
            return False, str(error)

    def get_deleted_qr_codes(self, limit: int = 50) -> List[QRModel]:
        """Get soft-deleted QR codes."""
        try:
            db = self.storage.db
            collection = db[QRModel.COLLECTION_NAME]
            documents = collection.find(
                {"status": "deleted"}
            ).limit(limit).sort("updated_at", -1)
            return [QRModel.from_dict(doc) for doc in documents]
        except Exception:
            return []

    def search_history(self, query: str, limit: int = 50) -> List[QRModel]:
        """Search QR code history."""
        return self.storage.search_qr(query, limit=limit)

    def get_most_used_qr_types(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get the most frequently used QR types."""
        stats = self.storage.get_statistics()
        type_dist = stats.get("type_distribution", [])
        return type_dist[:limit]

    def get_most_scanned_qr(self, limit: int = 10) -> List[QRModel]:
        """Get the most scanned QR codes."""
        all_qr = self.storage.get_all_qr(limit=1000)
        return sorted(all_qr, key=lambda x: x.scan_count, reverse=True)[:limit]

    def get_most_exported_qr(self, limit: int = 10) -> List[QRModel]:
        """Get the most exported QR codes."""
        all_qr = self.storage.get_all_qr(limit=1000)
        return sorted(all_qr, key=lambda x: x.export_count, reverse=True)[:limit]

    def delete_qr_permanently(self, qr_id: str) -> tuple[bool, str]:
        """Permanently delete a QR code from the database."""
        try:
            db = self.storage.db
            collection = db[QRModel.COLLECTION_NAME]
            from bson.objectid import ObjectId
            result = collection.delete_one({"_id": ObjectId(qr_id)})
            if result.deleted_count == 0:
                return False, "QR code not found."
            return True, "Permanently deleted."
        except Exception as error:
            return False, str(error)

    def get_statistics(self) -> Dict[str, Any]:
        """Get history statistics."""
        return self.storage.get_statistics()
