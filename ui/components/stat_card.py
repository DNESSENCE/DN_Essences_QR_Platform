import customtkinter as ctk

from config.theme import CARD, TEXT, TEXT_SECONDARY, ACCENT


class StatCard(ctk.CTkFrame):
    """
    Reusable Dashboard Statistic Card
    """

    def __init__(
        self,
        master,
        title: str,
        value: str = "0",
        icon: str = "📊"
    ):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
            height=140
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        # ------------------------
        # Icon
        # ------------------------

        self.icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 26)
        )

        self.icon_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=18,
            pady=(18, 0)
        )

        # ------------------------
        # Value
        # ------------------------

        self.value_label = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 34, "bold"),
            text_color=TEXT
        )

        self.value_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=18,
            pady=(6, 0)
        )

        # ------------------------
        # Title
        # ------------------------

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 14),
            text_color=TEXT_SECONDARY
        )

        self.title_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=18,
            pady=(0, 18)
        )

    # ---------------------------------

    def set_value(self, value):

        self.value_label.configure(
            text=str(value)
        )

    # ---------------------------------

    def set_title(self, title):

        self.title_label.configure(
            text=title
        )

    # ---------------------------------

    def set_icon(self, icon):

        self.icon_label.configure(
            text=icon
        )