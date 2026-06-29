import customtkinter as ctk

from config.theme import PRIMARY

from controllers.dashboard_controller import DashboardController

from ui.components.stat_card import StatCard
from ui.components.database_card import DatabaseCard
from ui.components.quick_action import QuickAction
from ui.components.activity_table import ActivityTable
from ui.components.notification_card import NotificationCard


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=PRIMARY
        )

        # ======================================================
        # GRID CONFIGURATION
        # ======================================================

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)

        # ======================================================
        # BUILD UI
        # ======================================================

        self.create_header()

        self.create_statistics()

        self.create_middle_section()

        self.create_bottom_section()

        # ======================================================
        # CONTROLLER
        # ======================================================

        self.controller = DashboardController(self)

        self.controller.refresh()

    # ==========================================================
    # HEADER
    # ==========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(10, 20)
        )

        header.grid_columnconfigure(1, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Dashboard",
            font=("Segoe UI", 30, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.connection_label = ctk.CTkLabel(
            header,
            text="🟢 Connected",
            font=("Segoe UI", 16)
        )

        self.connection_label.grid(
            row=0,
            column=1,
            sticky="e"
        )

    # ==========================================================
    # STATISTICS
    # ==========================================================

    def create_statistics(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)

        self.qr_card = StatCard(
            frame,
            title="QR Codes",
            value="0",
            icon="🔳"
        )

        self.qr_card.grid(
            row=0,
            column=0,
            padx=8,
            sticky="nsew"
        )

        self.scan_card = StatCard(
            frame,
            title="Total Scans",
            value="0",
            icon="📊"
        )

        self.scan_card.grid(
            row=0,
            column=1,
            padx=8,
            sticky="nsew"
        )

        self.export_card = StatCard(
            frame,
            title="Total Exports",
            value="0",
            icon="💾"
        )

        self.export_card.grid(
            row=0,
            column=2,
            padx=8,
            sticky="nsew"
        )

        self.customer_card = StatCard(
            frame,
            title="Customers",
            value="0",
            icon="👥"
        )

        self.customer_card.grid(
            row=0,
            column=3,
            padx=8,
            sticky="nsew"
        )

        self.product_card = StatCard(
            frame,
            title="Products",
            value="0",
            icon="👕"
        )

        self.product_card.grid(
            row=0,
            column=4,
            padx=8,
            sticky="nsew"
        )

    # ==========================================================
    # MIDDLE SECTION
    # ==========================================================

    def create_middle_section(self):

        middle = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        middle.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=20
        )

        middle.grid_columnconfigure(0, weight=1)
        middle.grid_columnconfigure(1, weight=2)

        # -------------------------
        # Quick Action
        # -------------------------

        self.quick_action = QuickAction(
            middle
        )

        self.quick_action.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # -------------------------
        # Database Card
        # -------------------------

        self.database_card = DatabaseCard(
            middle
        )

        self.database_card.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # ==========================================================
    # BOTTOM SECTION
    # ==========================================================

    def create_bottom_section(self):

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

        bottom.grid_columnconfigure(0, weight=2)
        bottom.grid_columnconfigure(1, weight=1)

        bottom.grid_rowconfigure(0, weight=1)

        # -------------------------
        # Activity
        # -------------------------

        self.activity_table = ActivityTable(
            bottom
        )

        self.activity_table.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # -------------------------
        # Notification
        # -------------------------

        self.notification = NotificationCard(
            bottom
        )

        self.notification.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # ==========================================================
    # REFRESH DASHBOARD
    # ==========================================================

    def refresh(self):

        self.controller.refresh()