import customtkinter as ctk

from config.theme import *


class QROptions(ctk.CTkFrame):
    """
    QR Customization Panel

    Part 5.1
    ----------
    • Foreground Color
    • Background Color
    • QR Size
    • Border Size

    Part 5.2
    ----------
    • Controller Integration

    Part 5.3
    ----------
    • Live Preview Updates
    """

    FOREGROUND_COLORS = [
        "Black",
        "Blue",
        "Red",
        "Green",
        "Purple"
    ]

    BACKGROUND_COLORS = [
        "White",
        "Light Gray",
        "Yellow",
        "Light Blue"
    ]

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155"
        )

        self.create_widgets()

    # ==========================================================
    # UI
    # ==========================================================

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Customization",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 20)
        )

        # ------------------------------------------------------

        ctk.CTkLabel(
            self,
            text="Foreground Color"
        ).pack(
            anchor="w",
            padx=20
        )

        self.foreground = ctk.CTkComboBox(
            self,
            values=self.FOREGROUND_COLORS,
            state="readonly"
        )

        self.foreground.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        self.foreground.set("Black")

        # ------------------------------------------------------

        ctk.CTkLabel(
            self,
            text="Background Color"
        ).pack(
            anchor="w",
            padx=20
        )

        self.background = ctk.CTkComboBox(
            self,
            values=self.BACKGROUND_COLORS,
            state="readonly"
        )

        self.background.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        self.background.set("White")

        # ------------------------------------------------------

        ctk.CTkLabel(
            self,
            text="QR Size"
        ).pack(
            anchor="w",
            padx=20
        )

        self.size = ctk.CTkSlider(
            self,
            from_=4,
            to=20,
            number_of_steps=16
        )

        self.size.pack(
            fill="x",
            padx=20,
            pady=(5, 5)
        )

        self.size.set(10)

        self.size_label = ctk.CTkLabel(
            self,
            text="10"
        )

        self.size_label.pack(
            anchor="e",
            padx=20,
            pady=(0, 15)
        )

        self.size.configure(
            command=self.update_size
        )

        # ------------------------------------------------------

        ctk.CTkLabel(
            self,
            text="Border Size"
        ).pack(
            anchor="w",
            padx=20
        )

        self.border = ctk.CTkSlider(
            self,
            from_=1,
            to=10,
            number_of_steps=9
        )

        self.border.pack(
            fill="x",
            padx=20,
            pady=(5, 5)
        )

        self.border.set(4)

        self.border_label = ctk.CTkLabel(
            self,
            text="4"
        )

        self.border_label.pack(
            anchor="e",
            padx=20,
            pady=(0, 20)
        )

        self.border.configure(
            command=self.update_border
        )

        # ------------------------------------------------------

        self.reset_btn = ctk.CTkButton(
            self,
            text="Reset Customization",
            height=40
        )

        self.reset_btn.pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

    # ==========================================================
    # Slider Updates
    # ==========================================================

    def update_size(self, value):

        self.size_label.configure(
            text=str(int(value))
        )

    def update_border(self, value):

        self.border_label.configure(
            text=str(int(value))
        )

    # ==========================================================
    # Get Values
    # ==========================================================

    def get_options(self):

        return {

            "foreground": self.foreground.get(),

            "background": self.background.get(),

            "size": int(self.size.get()),

            "border": int(self.border.get())

        }

    # ==========================================================
    # Reset
    # ==========================================================

    def reset(self):

        self.foreground.set("Black")

        self.background.set("White")

        self.size.set(10)

        self.border.set(4)

        self.size_label.configure(text="10")

        self.border_label.configure(text="4")

    # ==========================================================
    # Callback
    # ==========================================================

    def set_reset_callback(self, callback):

        self.reset_btn.configure(
            command=callback
        )