import re
from typing import Any, Dict, List, Optional

import qrcode
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H
from qrcode.constants import ERROR_CORRECT_L
from qrcode.constants import ERROR_CORRECT_M
from qrcode.constants import ERROR_CORRECT_Q


class QRService:
    """Commercial QR generation engine for the D&N Essences platform."""

    ERROR_LEVELS = {
        "L": ERROR_CORRECT_L,
        "M": ERROR_CORRECT_M,
        "Q": ERROR_CORRECT_Q,
        "H": ERROR_CORRECT_H,
    }

    COLOR_MAP = {
        "Black": "#000000",
        "Blue": "#2563EB",
        "Red": "#DC2626",
        "Green": "#16A34A",
        "Purple": "#9333EA",
        "White": "#FFFFFF",
        "Light Gray": "#E5E7EB",
        "Yellow": "#FEF08A",
        "Light Blue": "#BFDBFE",
    }

    def generate(
        self,
        qr_type: str,
        value: str,
        foreground: str = "Black",
        background: str = "White",
        size: int = 10,
        border: int = 4,
        error: str = "M",
        version: Optional[int] = None,
        fit: bool = True,
    ) -> Image.Image:
        """Generate a QR code image for the given input."""
        payload = self.build_qr_data(
            qr_type=qr_type,
            value=value,
            foreground=foreground,
            background=background,
            size=size,
            border=border,
            error=error,
            version=version,
            fit=fit,
        )
        return self.create_qr(payload)

    def format_data(self, qr_type: str, value: str) -> str:
        """Transform the user input into a QR-ready payload."""
        normalized_type = (qr_type or "").strip().lower()
        cleaned_value = (value or "").strip()

        if "website" in normalized_type:
            return self.generate_website(cleaned_value)
        if "instagram" in normalized_type:
            return self.generate_instagram(cleaned_value)
        if "whatsapp" in normalized_type:
            return self.generate_whatsapp(cleaned_value)
        if "email" in normalized_type:
            return self.generate_email(cleaned_value)
        if "phone" in normalized_type:
            return self.generate_phone(cleaned_value)
        return cleaned_value

    def generate_website(self, url: str) -> str:
        """Ensure website URLs are prefixed with https:// when missing."""
        cleaned_url = (url or "").strip()
        if not cleaned_url:
            raise ValueError("Website URL cannot be empty.")
        if not cleaned_url.startswith(("http://", "https://")):
            cleaned_url = f"https://{cleaned_url}"
        return cleaned_url

    def generate_instagram(self, username: str) -> str:
        """Normalize Instagram handles or URLs into a valid Instagram link."""
        cleaned_username = (username or "").strip()
        if not cleaned_username:
            raise ValueError("Instagram value cannot be empty.")
        if cleaned_username.startswith("http"):
            return cleaned_username
        normalized_username = cleaned_username.replace("@", "").strip("/")
        return f"https://instagram.com/{normalized_username}"

    def generate_whatsapp(self, number: str) -> str:
        """Create a wa.me link from a phone number."""
        cleaned_number = (number or "").strip()
        if not cleaned_number:
            raise ValueError("WhatsApp number cannot be empty.")
        digits = re.sub(r"\D", "", cleaned_number)
        if not digits:
            raise ValueError("WhatsApp number must contain digits.")
        return f"https://wa.me/{digits}"

    def generate_email(self, email: str) -> str:
        """Create a mailto link for email QR codes."""
        cleaned_email = (email or "").strip()
        if not cleaned_email:
            raise ValueError("Email address cannot be empty.")
        return f"mailto:{cleaned_email}"

    def generate_phone(self, phone: str) -> str:
        """Create a tel link for phone QR codes."""
        cleaned_phone = (phone or "").strip()
        if not cleaned_phone:
            raise ValueError("Phone number cannot be empty.")
        if not cleaned_phone.startswith("+"):
            cleaned_phone = f"+{cleaned_phone}"
        return f"tel:{cleaned_phone}"

    def create_qr(self, payload: Dict[str, Any]) -> Image.Image:
        """Build the final PIL image for the QR code."""
        data = payload["formatted_value"]
        error_level = self.ERROR_LEVELS.get(
            (payload.get("error_correction") or "M").upper(),
            ERROR_CORRECT_M,
        )
        size = max(1, int(payload.get("size", 10)))
        border = max(0, int(payload.get("border", 4)))
        version = payload.get("version")
        fit = bool(payload.get("fit", True))

        qr = qrcode.QRCode(
            version=version,
            error_correction=error_level,
            box_size=size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=fit)

        foreground_color = self._resolve_color(payload.get("foreground"), "#000000")
        background_color = self._resolve_color(payload.get("background"), "#FFFFFF")

        image = qr.make_image(
            fill_color=foreground_color,
            back_color=background_color,
        )

        if not hasattr(image, "convert"):
            raise TypeError("Generated QR image is not a Pillow image.")
        return image.convert("RGB")

    def build_qr_data(
        self,
        qr_type: str,
        value: str,
        foreground: str = "Black",
        background: str = "White",
        size: int = 10,
        border: int = 4,
        error: str = "M",
        version: Optional[int] = None,
        fit: bool = True,
    ) -> Dict[str, Any]:
        """Create a metadata dictionary for QR generation and future storage."""
        return {
            "qr_type": (qr_type or "").strip(),
            "raw_value": (value or "").strip(),
            "formatted_value": self.format_data(qr_type, value),
            "foreground": foreground,
            "background": background,
            "size": int(size),
            "border": int(border),
            "error_correction": (error or "M").upper(),
            "version": version,
            "fit": fit,
        }

    def supported_types(self) -> List[str]:
        """Return the supported QR types."""
        return ["Website", "Instagram", "WhatsApp", "Email", "Phone"]

    def _resolve_color(self, color: Optional[str], fallback: str) -> str:
        """Resolve a color name or hex code into a valid QR color."""
        if not color:
            return fallback
        normalized_color = str(color).strip()
        if normalized_color in self.COLOR_MAP:
            return self.COLOR_MAP[normalized_color]
        if normalized_color.startswith("#"):
            return normalized_color
        return fallback

    def generate_dnessence_instagram(self) -> Image.Image:
        """Create a branded Instagram QR for D&N Essences."""
        return self.generate(qr_type="Instagram", value="_dnessence_")

    def generate_dnessence_website(self, website: str) -> Image.Image:
        """Create a branded website QR for D&N Essences."""
        return self.generate(qr_type="Website", value=website)