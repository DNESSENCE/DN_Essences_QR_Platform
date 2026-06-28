import customtkinter as ctk

from config.theme import *


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            width=240,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_propagate(False)

        buttons = [
            "Dashboard",
            "QR Generator",
            "History",
            "Analytics",
            "Settings"
        ]

        for name in buttons:

            button = ctk.CTkButton(
                self,
                text=name,
                fg_color="transparent",
                hover_color=ACCENT,
                anchor="w"
            )

            button.pack(
                fill="x",
                padx=15,
                pady=8
            )