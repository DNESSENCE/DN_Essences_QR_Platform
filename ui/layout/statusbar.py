import customtkinter as ctk

from config.theme import *


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            height=30,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        label = ctk.CTkLabel(
            self,
            text="MongoDB Connected | Ready",
            anchor="w"
        )

        label.pack(
            fill="x",
            padx=15
        )