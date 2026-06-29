import customtkinter as ctk

from config.theme import CARD, ACCENT, TEXT


class QuickAction(ctk.CTkFrame):
    """
    Quick Action Panel
    """

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
            text="Quick Actions",
            font=("Segoe UI", 20, "bold"),
            text_color=TEXT
        )

        title.pack(anchor="w", padx=20, pady=(20, 15))

        self.buttons = {}

        actions = [

            ("➕ Generate QR", None),

            ("📜 History", None),

            ("👕 Products", None),

            ("👥 Customers", None),

            ("⚙ Settings", None)

        ]

        for text, command in actions:

            button = ctk.CTkButton(

                self,

                text=text,

                command=command,

                fg_color=ACCENT,

                height=42,

                corner_radius=10,

                anchor="w"

            )

            button.pack(

                fill="x",

                padx=20,

                pady=5

            )

            self.buttons[text] = button

    def bind_action(self, name, callback):

        if name in self.buttons:

            self.buttons[name].configure(

                command=callback

            )