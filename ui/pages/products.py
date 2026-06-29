import customtkinter as ctk


class ProductsPage(ctk.CTkFrame):

    def __init__(

        self,

        master

    ):

        super().__init__(master)

        label = ctk.CTkLabel(

            self,

            text="Products",

            font=("Segoe UI", 30, "bold")

        )

        label.pack(

            pady=50

        )