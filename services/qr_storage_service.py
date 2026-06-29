from datetime import datetime
from typing import List, Optional, Dict, Any

from bson.objectid import ObjectId
from database.mongodb import get_database
from models.qr_model import QRModel


class QRStorageService:
    """Service for QR code persistence and retrieval from MongoDB."""

    def __init__(self):
        self.db = get_database()
        self.collection = self.db[QRModel.COLLECTION_NAME]
        self._ensure_indexes()

    def save_qr(self, qr_model: QRModel) -> tuple[bool, str]:
        """Save a new QR code to MongoDB."""
        try:
            if not qr_model:
                return False, "Invalid QR model."
            
            if self._qr_exists(qr_model.formatted_value):
                return False, "QR code with this data already exists."

            result = self.collection.insert_one(qr_model.to_dict())
            qr_model._id = result.inserted_id
            return True, str(result.inserted_id)
        except Exception as error:
            return False, f"Save failed: {str(error)}"

    def update_qr(self, qr_id: str, update_data: Dict[str, Any]) -> tuple[bool, str]:
        """Update an existing QR code."""
        try:
            if not qr_id or not update_data:
                return False, "Invalid parameters."

            object_id = ObjectId(qr_id)
            update_data["updated_at"] = datetime.utcnow()

            result = self.collection.update_one(
                {"_id": object_id},
                {"$set": update_data}
            )

            if result.matched_count == 0:
                return False, "QR code not found."
            
            return True, "Updated successfully."
        except Exception as error:
            return False, f"Update failed: {str(error)}"

    def delete_qr(self, qr_id: str) -> tuple[bool, str]:
        """Mark a QR code as deleted (soft delete)."""
        try:
            if not qr_id:
                return False, "Invalid QR ID."

            object_id = ObjectId(qr_id)
            result = self.collection.update_one(
                {"_id": object_id},
                {"$set": {"status": "deleted", "updated_at": datetime.utcnow()}}
            )

            if result.matched_count == 0:
                return False, "QR code not found."
            
            return True, "Deleted successfully."
        except Exception as error:
            return False, f"Delete failed: {str(error)}"

    def get_qr(self, qr_id: str) -> Optional[QRModel]:
        """Retrieve a QR code by ID."""
        try:
            if not qr_id:
                return None

            object_id = ObjectId(qr_id)
            document = self.collection.find_one(
                {"_id": object_id, "status": {"$ne": "deleted"}}
            )
            
            if document:
                return QRModel.from_dict(document)
            return None
        except Exception:
            return None

    def get_all_qr(self, limit: int = 100, skip: int = 0) -> List[QRModel]:
        """Retrieve all active QR codes with pagination."""
        try:
            documents = self.collection.find(
                {"status": {"$ne": "deleted"}}
            ).skip(skip).limit(limit).sort("created_at", -1)
            
            return [QRModel.from_dict(doc) for doc in documents]
        except Exception:
            return []

    def get_qr_by_type(self, qr_type: str, limit: int = 50) -> List[QRModel]:
        """Retrieve QR codes by type."""
        try:
            if not qr_type:
                return []

            documents = self.collection.find(
                {"qr_type": qr_type, "status": {"$ne": "deleted"}}
            ).limit(limit).sort("created_at", -1)
            
            return [QRModel.from_dict(doc) for doc in documents]
        except Exception:
            return []

    def increment_scan(self, qr_id: str) -> tuple[bool, str]:
        """Increment the scan count for a QR code."""
        try:
            if not qr_id:
                return False, "Invalid QR ID."

            object_id = ObjectId(qr_id)
            result = self.collection.update_one(
                {"_id": object_id},
                {
                    "$inc": {"scan_count": 1},
                    "$set": {"updated_at": datetime.utcnow()}
                }
            )

            if result.matched_count == 0:
                return False, "QR code not found."
            
            return True, "Scan count incremented."
        except Exception as error:
            return False, f"Increment failed: {str(error)}"

    def increment_export(self, qr_id: str) -> tuple[bool, str]:
        """Increment the export count for a QR code."""
        try:
            if not qr_id:
                return False, "Invalid QR ID."

            object_id = ObjectId(qr_id)
            result = self.collection.update_one(
                {"_id": object_id},
                {
                    "$inc": {"export_count": 1},
                    "$set": {"updated_at": datetime.utcnow()}
                }
            )

            if result.matched_count == 0:
                return False, "QR code not found."
            
            return True, "Export count incremented."
        except Exception as error:
            return False, f"Increment failed: {str(error)}"

    def search_qr(self, query: str, limit: int = 50) -> List[QRModel]:
        """Search QR codes by raw_value or notes."""
        try:
            if not query:
                return []

            search_pattern = {"$regex": query, "$options": "i"}
            documents = self.collection.find(
                {
                    "$and": [
                        {"status": {"$ne": "deleted"}},
                        {
                            "$or": [
                                {"raw_value": search_pattern},
                                {"formatted_value": search_pattern},
                                {"notes": search_pattern}
                            ]
                        }
                    ]
                }
            ).limit(limit).sort("created_at", -1)
            
            return [QRModel.from_dict(doc) for doc in documents]
        except Exception:
            return []

    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about QR codes."""
        try:
            total = self.collection.count_documents({"status": {"$ne": "deleted"}})
            
            type_stats = list(self.collection.aggregate([
                {"$match": {"status": {"$ne": "deleted"}}},
                {"$group": {"_id": "$qr_type", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]))
            
            total_scans = sum(
                doc.get("scan_count", 0) 
                for doc in self.collection.find(
                    {"status": {"$ne": "deleted"}},
                    {"scan_count": 1}
                )
            )
            
            total_exports = sum(
                doc.get("export_count", 0) 
                for doc in self.collection.find(
                    {"status": {"$ne": "deleted"}},
                    {"export_count": 1}
                )
            )
            
            return {
                "total_qr_codes": total,
                "total_scans": total_scans,
                "total_exports": total_exports,
                "type_distribution": type_stats,
            }
        except Exception:
            return {
                "total_qr_codes": 0,
                "total_scans": 0,
                "total_exports": 0,
                "type_distribution": [],
            }

    def _qr_exists(self, formatted_value: str) -> bool:
        """Check if a QR code with the same formatted value already exists."""
        try:
            return self.collection.find_one(
                {"formatted_value": formatted_value, "status": {"$ne": "deleted"}}
            ) is not None
        except Exception:
            return False

    def _ensure_indexes(self) -> None:
        """Create database indexes for performance."""
        try:
            self.collection.create_index("qr_type")
            self.collection.create_index("formatted_value")
            self.collection.create_index("created_at")
            self.collection.create_index("status")
            self.collection.create_index([("raw_value", "text"), ("notes", "text")])
        except Exception:
            pass
