from datetime import datetime
from typing import Optional, Dict, Any


class QRModel:
    """Data model for QR code storage in MongoDB."""

    COLLECTION_NAME = "qr_codes"

    def __init__(
        self,
        qr_type: str,
        raw_value: str,
        formatted_value: str,
        foreground_color: str = "Black",
        background_color: str = "White",
        border: int = 4,
        size: int = 10,
        created_by: Optional[str] = None,
        status: str = "active",
    ):
        self._id: Optional[str] = None
        self.qr_type = qr_type
        self.raw_value = raw_value
        self.formatted_value = formatted_value
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.border = border
        self.size = size
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.scan_count = 0
        self.export_count = 0
        self.created_by = created_by or "system"
        self.status = status
        self.tags: list = []
        self.notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to MongoDB document dictionary."""
        doc = {
            "qr_type": self.qr_type,
            "raw_value": self.raw_value,
            "formatted_value": self.formatted_value,
            "foreground_color": self.foreground_color,
            "background_color": self.background_color,
            "border": self.border,
            "size": self.size,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "scan_count": self.scan_count,
            "export_count": self.export_count,
            "created_by": self.created_by,
            "status": self.status,
            "tags": self.tags,
            "notes": self.notes,
        }
        if self._id:
            doc["_id"] = self._id
        return doc

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "QRModel":
        """Create a model instance from a MongoDB document."""
        instance = cls(
            qr_type=data.get("qr_type", ""),
            raw_value=data.get("raw_value", ""),
            formatted_value=data.get("formatted_value", ""),
            foreground_color=data.get("foreground_color", "Black"),
            background_color=data.get("background_color", "White"),
            border=data.get("border", 4),
            size=data.get("size", 10),
            created_by=data.get("created_by", "system"),
            status=data.get("status", "active"),
        )
        instance._id = data.get("_id")
        instance.created_at = data.get("created_at", datetime.utcnow())
        instance.updated_at = data.get("updated_at", datetime.utcnow())
        instance.scan_count = data.get("scan_count", 0)
        instance.export_count = data.get("export_count", 0)
        instance.tags = data.get("tags", [])
        instance.notes = data.get("notes", "")
        return instance

    def __repr__(self) -> str:
        return f"<QRModel {self.qr_type}:{self.raw_value}>"
