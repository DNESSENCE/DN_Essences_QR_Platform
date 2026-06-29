import customtkinter as ctk
from PIL import Image

from config.theme import CARD, PRIMARY


class QRPreview(ctk.CTkFrame):
    """Professional preview panel with cached QR rendering."""

    PREVIEW_SIZE = 320

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )
        self.image = None
        self.original_image = None
        self.ctk_image = None
        self.create_widgets()

    def create_widgets(self) -> None:
        title = ctk.CTkLabel(
            self,
            text="Live Preview",
            font=("Segoe UI", 22, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(20, 15))

        self.preview_frame = ctk.CTkFrame(
            self,
            width=360,
            height=360,
            fg_color=PRIMARY,
            corner_radius=12,
        )
        self.preview_frame.pack(expand=True, fill="both", padx=20, pady=10)
        self.preview_frame.pack_propagate(False)

        self.preview_label = ctk.CTkLabel(
            self.preview_frame,
            text="QR Preview",
            font=("Segoe UI", 20),
        )
        self.preview_label.pack(expand=True)

        self.info = ctk.CTkLabel(
            self,
            text="Generate a QR code to preview it here.",
            justify="center",
        )
        self.info.pack(pady=(5, 20))

    def show_image(self, image: Image.Image) -> None:
        """Render the generated QR on the preview widget without recreating widgets."""
        if image is None:
            self.set_placeholder()
            return

        self.original_image = image.copy()
        resized_image = self.thumbnail(image, self.PREVIEW_SIZE)
        self.ctk_image = ctk.CTkImage(light_image=resized_image, size=(self.PREVIEW_SIZE, self.PREVIEW_SIZE))
        self.image = resized_image

        self.preview_label.configure(image=self.ctk_image, text="")

    def clear(self) -> None:
        """Clear the preview and reset placeholder state."""
        self.preview_label.configure(image=None, text="QR Preview")
        self.image = None
        self.original_image = None
        self.ctk_image = None

    def set_placeholder(self) -> None:
        """Restore the default placeholder view."""
        self.preview_label.configure(image=None, text="QR Preview")
        self.info.configure(text="Generate a QR code to preview it here.")

    def set_status(self, message: str) -> None:
        """Set the preview status text."""
        self.info.configure(text=message)

    def thumbnail(self, image: Image.Image, size: int) -> Image.Image:
        """Return a resized image that preserves aspect ratio and quality."""
        if image is None:
            return None
        if image.mode != "RGB":
            image = image.convert("RGB")
        width, height = image.size
        if width <= size and height <= size:
            return image
        return image.resize((size, size), Image.Resampling.LANCZOS)