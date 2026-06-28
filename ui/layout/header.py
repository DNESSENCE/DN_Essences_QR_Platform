import customtkinter as ctk

from config.theme import *
from config.app_config import *


class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            height=70,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_columnconfigure(1, weight=1)

        title = ctk.CTkLabel(
            self,
            text=APP_NAME,
            font=("Segoe UI", 24, "bold")
        )

        title.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="w"
        )

        version = ctk.CTkLabel(
            self,
            text=VERSION,
            font=("Segoe UI", 14)
        )

        version.grid(
            row=0,
            column=2,
            padx=20
        )