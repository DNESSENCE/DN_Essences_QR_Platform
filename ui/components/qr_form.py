import customtkinter as ctk

from config.theme import CARD, PRIMARY


class QRForm(ctk.CTkFrame):
    """Professional input form for QR generation."""

    QR_TYPES = [
        "🌐 Website",
        "📷 Instagram",
        "💬 WhatsApp",
        "📧 Email",
        "📞 Phone",
    ]

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self) -> None:
        title = ctk.CTkLabel(
            self,
            text="QR Information",
            font=("Segoe UI", 22, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(20, 15))

        type_label = ctk.CTkLabel(self, text="QR Type")
        type_label.pack(anchor="w", padx=20)

        self.qr_type = ctk.CTkComboBox(
            self,
            values=self.QR_TYPES,
            state="readonly",
            width=260,
        )
        self.qr_type.pack(fill="x", padx=20, pady=(5, 15))
        self.qr_type.set(self.QR_TYPES[0])

        self.input_title = ctk.CTkLabel(self, text="Website URL")
        self.input_title.pack(anchor="w", padx=20)

        self.input_entry = ctk.CTkEntry(
            self,
            placeholder_text="https://example.com",
            height=40,
        )
        self.input_entry.pack(fill="x", padx=20, pady=(5, 15))
        self.input_entry.bind("<Return>", self._handle_enter_key)

        self.description = ctk.CTkLabel(
            self,
            text="Enter the data that should be encoded into the QR code.",
            justify="left",
            wraplength=260,
        )
        self.description.pack(anchor="w", padx=20, pady=(0, 20))

        self.generate_btn = ctk.CTkButton(self, text="Generate QR", height=42)
        self.generate_btn.pack(fill="x", padx=20, pady=5)

        self.clear_btn = ctk.CTkButton(
            self,
            text="Clear",
            height=42,
            fg_color="#374151",
            hover_color="#4B5563",
        )
        self.clear_btn.pack(fill="x", padx=20, pady=5)

        self.save_btn = ctk.CTkButton(self, text="Save to Database", height=42)
        self.save_btn.pack(fill="x", padx=20, pady=5)

        self.export_btn = ctk.CTkButton(self, text="Export QR", height=42)
        self.export_btn.pack(fill="x", padx=20, pady=(5, 20))

        self.qr_type.configure(command=self.on_type_changed)
        self._update_placeholder()

    def on_type_changed(self, value: str) -> None:
        """Update the form labels and placeholders based on the selected QR type."""
        if "Website" in value:
            self.input_title.configure(text="Website URL")
            self.input_entry.configure(placeholder_text="https://example.com")
        elif "Instagram" in value:
            self.input_title.configure(text="Instagram Username / URL")
            self.input_entry.configure(placeholder_text="https://instagram.com/_dnessence_")
        elif "WhatsApp" in value:
            self.input_title.configure(text="WhatsApp Number")
            self.input_entry.configure(placeholder_text="+919876543210")
        elif "Email" in value:
            self.input_title.configure(text="Email Address")
            self.input_entry.configure(placeholder_text="hello@example.com")
        elif "Phone" in value:
            self.input_title.configure(text="Phone Number")
            self.input_entry.configure(placeholder_text="+919876543210")
        self._update_placeholder()

    def get_qr_type(self) -> str:
        """Return the currently selected QR type."""
        return self.qr_type.get()

    def get_data(self) -> str:
        """Return the current input value."""
        return self.input_entry.get().strip()

    def clear(self) -> None:
        """Clear the form entry field."""
        self.input_entry.delete(0, "end")

    def set_generate_callback(self, callback) -> None:
        """Set the callback for the generate action."""
        self.generate_btn.configure(command=callback)

    def set_clear_callback(self, callback) -> None:
        """Set the callback for the clear action."""
        self.clear_btn.configure(command=callback)

    def set_save_callback(self, callback) -> None:
        """Set the callback for the save action."""
        self.save_btn.configure(command=callback)

    def set_export_callback(self, callback) -> None:
        """Set the callback for the export action."""
        self.export_btn.configure(command=callback)

    def _handle_enter_key(self, _event) -> None:
        """Trigger generation when the Enter key is pressed."""
        if self.generate_btn.cget("command"):
            self.generate_btn.invoke()

    def _update_placeholder(self) -> None:
        """Ensure the input field placeholder matches the selected QR type."""
        current_type = self.get_qr_type()
        if "Website" in current_type:
            self.input_entry.configure(placeholder_text="https://example.com")
        elif "Instagram" in current_type:
            self.input_entry.configure(placeholder_text="https://instagram.com/_dnessence_")
        elif "WhatsApp" in current_type:
            self.input_entry.configure(placeholder_text="+919876543210")
        elif "Email" in current_type:
            self.input_entry.configure(placeholder_text="hello@example.com")
        elif "Phone" in current_type:
            self.input_entry.configure(placeholder_text="+919876543210")