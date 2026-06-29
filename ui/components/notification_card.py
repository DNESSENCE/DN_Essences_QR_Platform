import customtkinter as ctk

from config.theme import CARD, TEXT


class NotificationCard(ctk.CTkFrame):

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

            text="System Notifications",

            font=("Segoe UI", 20, "bold"),

            text_color=TEXT

        )

        title.pack(

            anchor="w",

            padx=20,

            pady=(20, 15)

        )

        self.box = ctk.CTkTextbox(

            self,

            height=160,

            border_width=0

        )

        self.box.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=(0, 20)

        )

        self.default_notifications()

    def default_notifications(self):

        self.box.delete(

            "1.0",

            "end"

        )

        notifications = [

            "🟢 MongoDB Connected",

            "✔ Application Ready",

            "✔ Waiting for first QR"

        ]

        for notification in notifications:

            self.box.insert(

                "end",

                notification + "\n"

            )

    def add_notification(self, message):

        self.box.insert(

            "end",

            message + "\n"

        )