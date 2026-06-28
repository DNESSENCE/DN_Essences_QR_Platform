import customtkinter as ctk

from config.app_config import *
from config.theme import *

from ui.layout.sidebar import Sidebar
from ui.layout.header import Header
from ui.layout.statusbar import StatusBar

from ui.pages.dashboard import DashboardPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)

        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.configure(fg_color=PRIMARY)

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(1, weight=1)

        self.header = Header(self)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=1, column=0, sticky="ns")

        self.content = ctk.CTkFrame(
            self,
            fg_color=PRIMARY,
            corner_radius=0
        )

        self.content.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.status = StatusBar(self)
        self.status.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        self.show_dashboard()

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):

        self.clear_content()

        DashboardPage(self.content).pack(
            fill="both",
            expand=True
        )