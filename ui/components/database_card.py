import customtkinter as ctk

from config.theme import CARD, TEXT, TEXT_SECONDARY, SUCCESS


class DatabaseCard(ctk.CTkFrame):
    """
    MongoDB Atlas Status Card
    """

    def __init__(

        self,

        master,

        status="Connected",

        database="dn_essences_qr",

        cluster="dn-essences-cluster"

    ):

        super().__init__(

            master,

            fg_color=CARD,

            corner_radius=15,

            border_width=1,

            border_color="#334155"

        )

        self.grid_columnconfigure(1, weight=1)

        # --------------------------
        # Title
        # --------------------------

        title = ctk.CTkLabel(

            self,

            text="MongoDB Atlas",

            font=("Segoe UI", 20, "bold"),

            text_color=TEXT

        )

        title.grid(

            row=0,

            column=0,

            columnspan=2,

            padx=20,

            pady=(18, 20),

            sticky="w"

        )

        # --------------------------
        # Status
        # --------------------------

        ctk.CTkLabel(

            self,

            text="Status",

            font=("Segoe UI", 14),

            text_color=TEXT_SECONDARY

        ).grid(

            row=1,

            column=0,

            padx=20,

            sticky="w"

        )

        self.status = ctk.CTkLabel(

            self,

            text=f"🟢 {status}",

            font=("Segoe UI", 14, "bold"),

            text_color=SUCCESS

        )

        self.status.grid(

            row=1,

            column=1,

            sticky="w"

        )

        # --------------------------
        # Database
        # --------------------------

        ctk.CTkLabel(

            self,

            text="Database",

            font=("Segoe UI", 14),

            text_color=TEXT_SECONDARY

        ).grid(

            row=2,

            column=0,

            padx=20,

            pady=8,

            sticky="w"

        )

        self.database = ctk.CTkLabel(

            self,

            text=database,

            font=("Segoe UI", 14),

            text_color=TEXT

        )

        self.database.grid(

            row=2,

            column=1,

            sticky="w"

        )

        # --------------------------
        # Cluster
        # --------------------------

        ctk.CTkLabel(

            self,

            text="Cluster",

            font=("Segoe UI", 14),

            text_color=TEXT_SECONDARY

        ).grid(

            row=3,

            column=0,

            padx=20,

            pady=8,

            sticky="w"

        )

        self.cluster = ctk.CTkLabel(

            self,

            text=cluster,

            font=("Segoe UI", 14),

            text_color=TEXT

        )

        self.cluster.grid(

            row=3,

            column=1,

            sticky="w"

        )

        # --------------------------
        # Refresh Button
        # --------------------------

        self.refresh_btn = ctk.CTkButton(

            self,

            text="Refresh",

            width=130,

            height=35

        )

        self.refresh_btn.grid(

            row=4,

            column=0,

            columnspan=2,

            pady=22

        )

    # -----------------------------------

    def update_status(

        self,

        connected=True

    ):

        if connected:

            self.status.configure(

                text="🟢 Connected",

                text_color=SUCCESS

            )

        else:

            self.status.configure(

                text="🔴 Disconnected",

                text_color="red"

            )

    # -----------------------------------

    def set_database(

        self,

        database

    ):

        self.database.configure(

            text=database

        )

    # -----------------------------------

    def set_cluster(

        self,

        cluster

    ):

        self.cluster.configure(

            text=cluster

        )