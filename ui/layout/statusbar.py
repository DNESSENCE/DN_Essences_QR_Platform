import customtkinter as ctk

from config.app_config import VERSION
from config.theme import SIDEBAR


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            height=28,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_columnconfigure(1, weight=1)

        self.status = ctk.CTkLabel(
            self,
            text="🟢 MongoDB Connected"
        )

        self.status.grid(
            row=0,
            column=0,
            padx=15,
            sticky="w"
        )

        self.ready = ctk.CTkLabel(
            self,
            text="Ready"
        )

        self.ready.grid(
            row=0,
            column=1
        )

        self.version = ctk.CTkLabel(
            self,
            text=VERSION
        )

        self.version.grid(
            row=0,
            column=2,
            padx=15,
            sticky="e"
        )

    # ----------------------------------

    def set_status(self, connected=True):

        if connected:

            self.status.configure(

                text="🟢 MongoDB Connected"

            )

        else:

            self.status.configure(

                text="🔴 MongoDB Disconnected"

            )