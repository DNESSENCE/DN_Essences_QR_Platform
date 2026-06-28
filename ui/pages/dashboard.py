import customtkinter as ctk

from config.theme import *


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color="transparent"
        )

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            anchor="w",
            pady=20
        )

        cards = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=12
        )

        cards.pack(
            fill="x",
            pady=10
        )

        label = ctk.CTkLabel(
            cards,
            text="Welcome to D&N Essences Smart QR Platform",
            font=("Segoe UI", 18)
        )

        label.pack(
            pady=40
        )