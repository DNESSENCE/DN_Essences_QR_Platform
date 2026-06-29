import customtkinter as ctk

from config.theme import ACCENT


class SidebarButton(ctk.CTkButton):

    def __init__(self, master, text, command):

        super().__init__(
            master=master,
            text=text,
            command=command,
            fg_color="transparent",
            hover_color=ACCENT,
            text_color="white",
            corner_radius=10,
            height=42,
            anchor="w",
            font=("Segoe UI", 15, "bold")
        )

    def activate(self):
        self.configure(
            fg_color=ACCENT,
            text_color="white"
        )

    def deactivate(self):
        self.configure(
            fg_color="transparent",
            text_color="white"
        )