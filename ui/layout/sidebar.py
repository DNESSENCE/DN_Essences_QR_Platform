import customtkinter as ctk

from config.theme import *
from ui.components.sidebar_button import SidebarButton


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=240,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_propagate(False)

        self.buttons = {}

        pages = [
            "Dashboard",
            "QR Generator",
            "History",
            "Analytics",
            "Customers",
            "Products",
            "Orders",
            "Settings"
        ]

        for page in pages:

            button = SidebarButton(
                self,
                text=page,
                command=lambda p=page: master.navigation.show(p)
            )

            button.pack(
                fill="x",
                padx=15,
                pady=6
            )

            self.buttons[page] = button

    def select(self, page):

        for button in self.buttons.values():
            button.deactivate()

        if page in self.buttons:
            self.buttons[page].activate()