import customtkinter as ctk


class OrdersPage(ctk.CTkFrame):

    def __init__(

        self,

        master

    ):

        super().__init__(master)

        label = ctk.CTkLabel(

            self,

            text="Orders",

            font=("Segoe UI", 30, "bold")

        )

        label.pack(

            pady=50

        )