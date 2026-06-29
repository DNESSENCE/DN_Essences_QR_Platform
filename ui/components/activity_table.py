import customtkinter as ctk

from config.theme import CARD, TEXT


class ActivityTable(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155"
        )

        title = ctk.CTkLabel(
            self,
            text="Recent Activity",
            font=("Segoe UI", 20, "bold"),
            text_color=TEXT
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        self.listbox = ctk.CTkTextbox(
            self,
            height=220,
            border_width=0
        )

        self.listbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.load_default()

    def load_default(self):

        self.listbox.delete("1.0", "end")

        logs = [

            "✔ Application Started",

            "✔ MongoDB Connected",

            "✔ Dashboard Loaded",

            "✔ Waiting for first QR"

        ]

        for log in logs:

            self.listbox.insert(

                "end",

                log + "\n"

            )

    def add_activity(self, message):

        self.listbox.insert(

            "end",

            message + "\n"

        )