from tkinter import messagebox
from typing import Any, Dict, Optional

from services.qr_service import QRService
from services.export_service import ExportService
from services.qr_storage_service import QRStorageService
from models.qr_model import QRModel


class QRController:
    """Controller for QR generation, validation, and UI state orchestration."""

    def __init__(self, page: Any) -> None:
        self.page = page
        self.service = QRService()
        self.export_service = ExportService()
        self.storage_service = QRStorageService()
        self.generated_image = None
        self.original_image = None
        self.qr_metadata: Optional[Dict[str, Any]] = None
        self.qr_type: Optional[str] = None
        self.saved_qr_id: Optional[str] = None

    def generate(self) -> None:
        """Read UI input, validate it, generate the QR, and update the preview."""
        qr_type = self.page.form.get_qr_type()
        value = self.page.form.get_data()
        options = self.page.options.get_options()

        if not self.validate(qr_type, value):
            return

        try:
            image = self.service.generate(
                qr_type=qr_type,
                value=value,
                foreground=options["foreground"],
                background=options["background"],
                size=options["size"],
                border=options["border"],
            )

            self.generated_image = image
            self.original_image = image.copy()
            self.qr_metadata = self.service.build_qr_data(
                qr_type=qr_type,
                value=value,
                foreground=options["foreground"],
                background=options["background"],
                size=options["size"],
                border=options["border"],
            )
            self.qr_type = qr_type

            self.page.preview.show_image(image)
            self.page.preview.set_status("QR generated successfully.")
        except ValueError as error:
            messagebox.showwarning("Validation", str(error))
        except Exception as error:
            messagebox.showerror("QR Generator", str(error))

    def validate(self, qr_type: str, value: str) -> bool:
        """Validate the current form input for the selected QR type."""
        cleaned_value = (value or "").strip()

        if not cleaned_value:
            messagebox.showwarning("Validation", "Please enter a value.")
            return False

        if "Website" in qr_type:
            if "." not in cleaned_value:
                messagebox.showwarning("Validation", "Please enter a valid website.")
                return False
        elif "Instagram" in qr_type:
            if len(cleaned_value) < 2:
                messagebox.showwarning("Validation", "Invalid Instagram username.")
                return False
        elif "WhatsApp" in qr_type:
            digits = cleaned_value.replace("+", "").replace(" ", "")
            if not digits.isdigit():
                messagebox.showwarning("Validation", "Invalid WhatsApp number.")
                return False
        elif "Email" in qr_type:
            if "@" not in cleaned_value:
                messagebox.showwarning("Validation", "Invalid email address.")
                return False
        elif "Phone" in qr_type:
            digits = cleaned_value.replace("+", "").replace(" ", "")
            if not digits.isdigit():
                messagebox.showwarning("Validation", "Invalid phone number.")
                return False

        return True

    def clear(self) -> None:
        """Clear the form, options, and preview state."""
        self.page.form.clear()
        self.page.options.reset()
        self.page.preview.clear()
        self.page.preview.set_status("Waiting for input...")
        self.generated_image = None
        self.original_image = None
        self.qr_metadata = None
        self.qr_type = None

    def save(self) -> None:
        """Save the generated QR code to MongoDB."""
        if self.generated_image is None or not self.qr_metadata:
            messagebox.showwarning("Save QR", "Generate a QR code before saving it.")
            return

        try:
            self.page.preview.set_status("Saving QR to database...")
            self.page.after(100)

            qr_model = QRModel(
                qr_type=self.qr_type or "Unknown",
                raw_value=self.qr_metadata.get("raw_value", ""),
                formatted_value=self.qr_metadata.get("formatted_value", ""),
                foreground_color=self.qr_metadata.get("foreground", "Black"),
                background_color=self.qr_metadata.get("background", "White"),
                border=self.qr_metadata.get("border", 4),
                size=self.qr_metadata.get("size", 10),
            )

            success, result = self.storage_service.save_qr(qr_model)

            if success:
                self.saved_qr_id = result
                messagebox.showinfo(
                    "Save Successful",
                    f"QR code saved to database successfully.\n\nID: {result}",
                )
                self.page.preview.set_status("QR saved to database.")
            else:
                messagebox.showerror("Save Error", result)
                self.page.preview.set_status("Save failed.")
        except Exception as error:
            messagebox.showerror("Save Error", str(error))
            self.page.preview.set_status("Save failed.")

    def export(self) -> None:
        """Export the generated QR image to PNG, PDF, or SVG format."""
        if self.generated_image is None:
            messagebox.showwarning("Export QR", "Generate a QR code before exporting it.")
            return

        export_format = self._get_export_format()
        if not export_format:
            return

        try:
            self.page.preview.set_status("Exporting QR...")
            self.page.after(100)

            metadata = {
                "qr_type": self.qr_type or "Unknown",
                "created_at": self._get_timestamp(),
            }

            if export_format.upper() == "PNG":
                success, result = self.export_service.export_png(self.original_image)
            elif export_format.upper() == "PDF":
                success, result = self.export_service.export_pdf(self.original_image, metadata=metadata)
            elif export_format.upper() == "SVG":
                success, result = self.export_service.export_svg(self.original_image)
            else:
                messagebox.showerror("Export", "Unsupported format.")
                return

            if success:
                messagebox.showinfo(
                    "Export Successful",
                    f"QR code exported successfully to:\n\n{result}",
                )
                self.page.preview.set_status("QR exported successfully.")
            else:
                messagebox.showerror("Export Error", result)
                self.page.preview.set_status("Export failed.")
        except Exception as error:
            messagebox.showerror("Export Error", str(error))
            self.page.preview.set_status("Export failed.")

    def _get_export_format(self) -> Optional[str]:
        """Prompt the user to select an export format."""
        try:
            from tkinter import simpledialog
            format_choice = simpledialog.askstring(
                "Export Format",
                "Select export format:\nPNG (default)\nPDF\nSVG\n\nEnter format (PNG/PDF/SVG):",
                initialvalue="PNG",
            )
            if format_choice and format_choice.upper() in ("PNG", "PDF", "SVG"):
                return format_choice.upper()
            return None
        except Exception:
            return "PNG"

    def _get_timestamp(self) -> str:
        """Get the current timestamp for metadata."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")