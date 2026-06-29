from tkinter import messagebox
from typing import Any, Optional, List
from datetime import datetime

from services.history_service import HistoryService
from models.qr_model import QRModel


class HistoryController:
    """Controller for QR history management."""

    def __init__(self, page: Any):
        self.page = page
        self.service = HistoryService()
        self.current_qr_list: List[QRModel] = []
        self.selected_qr: Optional[QRModel] = None
        self.refresh()

    def refresh(self) -> None:
        """Refresh the history display."""
        try:
            self.current_qr_list = self.service.get_recent_qr_codes(limit=100)
            self.update_table()
        except Exception as error:
            messagebox.showerror("Error", f"Failed to load history: {str(error)}")

    def search(self, query: str) -> None:
        """Search QR codes by query."""
        if not query.strip():
            self.refresh()
            return

        try:
            self.current_qr_list = self.service.search_history(query, limit=100)
            self.update_table()
        except Exception as error:
            messagebox.showerror("Error", f"Search failed: {str(error)}")

    def filter_by_type(self, qr_type: str) -> None:
        """Filter QR codes by type."""
        if not qr_type or qr_type == "All":
            self.refresh()
            return

        try:
            all_qr = self.service.get_recent_qr_codes(limit=100)
            self.current_qr_list = [qr for qr in all_qr if qr.qr_type == qr_type]
            self.update_table()
        except Exception as error:
            messagebox.showerror("Error", f"Filter failed: {str(error)}")

    def filter_by_date_range(self, start_date: datetime, end_date: datetime) -> None:
        """Filter QR codes by date range."""
        try:
            self.current_qr_list = self.service.get_qr_by_date_range(start_date, end_date)
            self.update_table()
        except Exception as error:
            messagebox.showerror("Error", f"Filter failed: {str(error)}")

    def select_qr(self, qr_id: str) -> None:
        """Select a QR code from the table."""
        try:
            self.selected_qr = self.service.storage.get_qr(str(qr_id))
        except Exception:
            self.selected_qr = None

    def duplicate_qr(self, qr_id: str) -> None:
        """Duplicate a QR code."""
        if not qr_id:
            messagebox.showwarning("Duplicate", "Select a QR code first.")
            return

        try:
            success, result = self.service.duplicate_qr(str(qr_id))
            if success:
                messagebox.showinfo(
                    "Success",
                    f"QR code duplicated successfully.\n\nNew ID: {result}"
                )
                self.refresh()
            else:
                messagebox.showerror("Error", result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def delete_qr(self, qr_id: str) -> None:
        """Delete (soft) a QR code."""
        if not qr_id:
            messagebox.showwarning("Delete", "Select a QR code first.")
            return

        if messagebox.askyesno("Confirm", "Delete this QR code?"):
            try:
                success, result = self.service.storage.delete_qr(str(qr_id))
                if success:
                    messagebox.showinfo("Success", "QR code deleted.")
                    self.refresh()
                else:
                    messagebox.showerror("Error", result)
            except Exception as error:
                messagebox.showerror("Error", str(error))

    def restore_qr(self, qr_id: str) -> None:
        """Restore a deleted QR code."""
        if not qr_id:
            messagebox.showwarning("Restore", "Select a QR code first.")
            return

        try:
            success, result = self.service.restore_deleted_qr(str(qr_id))
            if success:
                messagebox.showinfo("Success", "QR code restored.")
                self.refresh()
            else:
                messagebox.showerror("Error", result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def export_qr(self, qr_id: str) -> None:
        """Export a specific QR code (future implementation)."""
        if not qr_id:
            messagebox.showwarning("Export", "Select a QR code first.")
            return

        messagebox.showinfo("Coming Soon", "Export from history will be available soon.")

    def get_table_data(self) -> List[tuple]:
        """Get formatted data for the history table."""
        data = []
        for qr in self.current_qr_list:
            data.append((
                str(qr._id)[:8],
                qr.qr_type,
                qr.raw_value[:30] + "..." if len(qr.raw_value) > 30 else qr.raw_value,
                str(qr.scan_count),
                str(qr.export_count),
                qr.created_at.strftime("%Y-%m-%d %H:%M:%S") if qr.created_at else "N/A",
            ))
        return data

    def update_table(self) -> None:
        """Update the history table display."""
        if hasattr(self.page, "table") and self.page.table:
            self.page.table.update_data(self.get_table_data())
