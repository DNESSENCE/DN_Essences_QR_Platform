import customtkinter as ctk

from config.theme import PRIMARY
from controllers.qr_controller import QRController
from ui.components.qr_form import QRForm
from ui.components.qr_options import QROptions
from ui.components.qr_preview import QRPreview


class QRGeneratorPage(ctk.CTkFrame):
    """Professional three-column QR generation page."""

    def __init__(self, master):
        super().__init__(master, fg_color=PRIMARY)
        self.create_layout()
        self.controller = QRController(self)
        self.bind_events()

    def create_layout(self) -> None:
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=15, pady=(10, 20))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Smart QR Generator",
            font=("Segoe UI", 30, "bold"),
        )
        title.grid(row=0, column=0, sticky="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Generate QR Codes for D&N Essences",
            font=("Segoe UI", 15),
        )
        subtitle.grid(row=1, column=0, sticky="w")

        self.form = QRForm(self)
        self.form.grid(row=1, column=0, sticky="nsew", padx=(15, 8), pady=(0, 15))

        self.preview = QRPreview(self)
        self.preview.grid(row=1, column=1, sticky="nsew", padx=8, pady=(0, 15))

        self.options = QROptions(self)
        self.options.grid(row=1, column=2, sticky="nsew", padx=(8, 15), pady=(0, 15))

    def bind_events(self) -> None:
        self.form.set_generate_callback(self.generate_qr)
        self.form.set_clear_callback(self.clear_form)
        self.form.set_save_callback(self.save_qr)
        self.form.set_export_callback(self.export_qr)
        self.options.set_reset_callback(self.reset_options)

    def generate_qr(self) -> None:
        self.controller.generate()

    def clear_form(self) -> None:
        self.controller.clear()

    def save_qr(self) -> None:
        self.controller.save()

    def export_qr(self) -> None:
        self.controller.export()

    def reset_options(self) -> None:
        self.options.reset()
        self.preview.set_status("Customization reset.")