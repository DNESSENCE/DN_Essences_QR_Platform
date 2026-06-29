import customtkinter as ctk
from datetime import datetime

from config.app_config import APP_NAME, VERSION
from config.theme import SIDEBAR


class Header(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            height=70,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_columnconfigure(1, weight=1)

        self.title = ctk.CTkLabel(
            self,
            text=APP_NAME,
            font=("Segoe UI", 22, "bold")
        )

        self.title.grid(
            row=0,
            column=0,
            padx=20,
            sticky="w"
        )

        self.page = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 15)
        )

        self.page.grid(
            row=0,
            column=1
        )

        self.clock = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI", 14)
        )

        self.clock.grid(
            row=0,
            column=2,
            padx=20,
            sticky="e"
        )

        self.update_clock()

    # ----------------------------------

    def update_page(self, page):

        self.page.configure(text=page)

    # ----------------------------------

    def update_clock(self):

        current = datetime.now().strftime("%d %b %Y  %I:%M:%S %p")

        self.clock.configure(text=current)

        self.after(
            1000,
            self.update_clock
        )