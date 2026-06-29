import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


class ExportService:
    """Professional QR export engine supporting PNG, SVG, and PDF formats."""

    EXPORT_BASE_DIR = Path("exports")
    PNG_DIR = EXPORT_BASE_DIR / "png"
    SVG_DIR = EXPORT_BASE_DIR / "svg"
    PDF_DIR = EXPORT_BASE_DIR / "pdf"

    COMPRESSION_QUALITY = 95
    PDF_DPI = 300
    PNG_DPI = 300

    def __init__(self) -> None:
        self._ensure_directories()

    def export_png(
        self,
        image: Image.Image,
        filename: Optional[str] = None,
        quality: int = COMPRESSION_QUALITY,
    ) -> Tuple[bool, str]:
        """Export QR code as high-quality PNG."""
        try:
            if image is None:
                return False, "No image to export."
            if not isinstance(image, Image.Image):
                return False, "Invalid image format."

            filename = filename or self._generate_filename("png")
            filepath = self.PNG_DIR / filename

            if image.mode != "RGB":
                image = image.convert("RGB")

            image.save(
                filepath,
                format="PNG",
                optimize=True,
                quality=quality,
            )

            return True, str(filepath)
        except Exception as error:
            return False, f"PNG export failed: {str(error)}"

    def export_pdf(
        self,
        image: Image.Image,
        filename: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Tuple[bool, str]:
        """Export QR code as professional PDF with metadata."""
        try:
            if image is None:
                return False, "No image to export."
            if not isinstance(image, Image.Image):
                return False, "Invalid image format."

            filename = filename or self._generate_filename("pdf")
            filepath = self.PDF_DIR / filename

            if image.mode != "RGB":
                image = image.convert("RGB")

            page_width, page_height = letter
            pdf_canvas = canvas.Canvas(str(filepath), pagesize=letter)

            pdf_canvas.setTitle("D&N Essences QR Code")
            pdf_canvas.setAuthor("D&N Essences Platform")
            pdf_canvas.setSubject("QR Code Export")

            image_width = page_width - 40
            image_height = (image.height / image.width) * image_width
            if image_height > page_height - 80:
                image_height = page_height - 80
                image_width = (image.width / image.height) * image_height

            img_reader = ImageReader(image)
            x = (page_width - image_width) / 2
            y = page_height - image_height - 30

            pdf_canvas.drawImage(img_reader, x, y, width=image_width, height=image_height)

            if metadata:
                y_pos = 20
                font_size = 10
                pdf_canvas.setFont("Helvetica", font_size)

                if "qr_type" in metadata:
                    pdf_canvas.drawString(
                        20, y_pos, f"Type: {metadata['qr_type']}"
                    )
                    y_pos -= font_size + 2

                if "created_at" in metadata:
                    pdf_canvas.drawString(
                        20, y_pos, f"Created: {metadata['created_at']}"
                    )
                    y_pos -= font_size + 2

                pdf_canvas.drawString(20, y_pos, "© D&N Essences Smart QR Platform")

            pdf_canvas.save()
            return True, str(filepath)
        except Exception as error:
            return False, f"PDF export failed: {str(error)}"

    def export_svg(
        self,
        image: Image.Image,
        filename: Optional[str] = None,
    ) -> Tuple[bool, str]:
        """Export QR code as scalable SVG using PIL to base64 embedding."""
        try:
            if image is None:
                return False, "No image to export."
            if not isinstance(image, Image.Image):
                return False, "Invalid image format."

            filename = filename or self._generate_filename("svg")
            filepath = self.SVG_DIR / filename

            if image.mode != "RGB":
                image = image.convert("RGB")

            width, height = image.size

            temp_png = filepath.with_suffix(".png")
            image.save(str(temp_png), format="PNG")

            with open(temp_png, "rb") as f:
                import base64
                image_data = base64.b64encode(f.read()).decode("utf-8")

            svg_content = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <defs>
        <style type="text/css">
            <![CDATA[
                image {{ image-rendering: pixelated; }}
            ]]>
        </style>
    </defs>
    <image x="0" y="0" width="{width}" height="{height}" xlink:href="data:image/png;base64,{image_data}" />
</svg>'''

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(svg_content)

            temp_png.unlink()
            return True, str(filepath)
        except Exception as error:
            return False, f"SVG export failed: {str(error)}"

    def get_export_path(self, format_type: str) -> Path:
        """Get the export directory for the specified format."""
        format_type_lower = (format_type or "").lower().strip()
        if format_type_lower == "png":
            return self.PNG_DIR
        elif format_type_lower == "pdf":
            return self.PDF_DIR
        elif format_type_lower == "svg":
            return self.SVG_DIR
        return self.EXPORT_BASE_DIR

    def _generate_filename(self, format_type: str) -> str:
        """Generate a timestamped filename for the exported QR."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"qr_{timestamp}.{format_type.lower()}"

    def _ensure_directories(self) -> None:
        """Create export directories if they don't exist."""
        for directory in [self.PNG_DIR, self.SVG_DIR, self.PDF_DIR]:
            directory.mkdir(parents=True, exist_ok=True)
