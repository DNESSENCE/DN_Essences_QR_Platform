import customtkinter as ctk

from config.app_config import *
from config.theme import *

from controllers.navigation_controller import NavigationController

from ui.layout.sidebar import Sidebar
from ui.layout.header import Header
from ui.layout.statusbar import StatusBar

from ui.pages.dashboard import Dashboard
from ui.pages.qr_generator import QRGeneratorPage
from ui.pages.history import HistoryPage
from ui.pages.analytics import AnalyticsPage
from ui.pages.customers import CustomersPage
from ui.pages.products import ProductsPage
from ui.pages.orders import OrdersPage
from ui.pages.settings import SettingsPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ==========================================================
        # WINDOW CONFIGURATION
        # ==========================================================

        self.title(APP_NAME)

        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.configure(fg_color=PRIMARY)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ==========================================================
        # HEADER
        # ==========================================================

        self.header = Header(self)

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # ==========================================================
        # SIDEBAR
        # ==========================================================

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        # ==========================================================
        # CONTENT AREA
        # ==========================================================

        self.content_frame = ctk.CTkFrame(
            self,
            fg_color=PRIMARY,
            corner_radius=0
        )

        self.content_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.content_frame.grid_rowconfigure(
            0,
            weight=1
        )

        self.content_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # ==========================================================
        # STATUS BAR
        # ==========================================================

        self.status = StatusBar(self)

        self.status.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # ==========================================================
        # NAVIGATION
        # ==========================================================

        self.navigation = NavigationController(self)

        self.navigation.register(
            "Dashboard",
            Dashboard
        )

        self.navigation.register(
            "QR Generator",
            QRGeneratorPage
        )

        self.navigation.register(
            "History",
            HistoryPage
        )

        self.navigation.register(
            "Analytics",
            AnalyticsPage
        )

        self.navigation.register(
            "Customers",
            CustomersPage
        )

        self.navigation.register(
            "Products",
            ProductsPage
        )

        self.navigation.register(
            "Orders",
            OrdersPage
        )

        self.navigation.register(
            "Settings",
            SettingsPage
        )

        # ==========================================================
        # LOAD DEFAULT PAGE
        # ==========================================================

        self.navigation.show("Dashboard")

        # ==========================================================
        # AUTO REFRESH
        # ==========================================================

        self.start_auto_refresh()

    # ==========================================================
    # CLEAR CONTENT
    # ==========================================================

    def clear_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # ==========================================================
    # AUTO REFRESH START
    # ==========================================================

    def start_auto_refresh(self):

        self.refresh_dashboard()

    # ==========================================================
    # DASHBOARD REFRESH LOOP
    # ==========================================================

    def refresh_dashboard(self):

        try:

            if self.navigation.current_page == "Dashboard":

                pages = self.content_frame.winfo_children()

                if pages:

                    dashboard = pages[0]

                    if hasattr(dashboard, "refresh"):

                        dashboard.refresh()

        except Exception as error:

            print(f"[Dashboard Refresh Error] {error}")

        finally:

            self.after(
                5000,
                self.refresh_dashboard
            )