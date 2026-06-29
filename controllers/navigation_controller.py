from typing import Dict, Type

import customtkinter as ctk


class NavigationController:

    def __init__(self, app):

        self.app = app

        self.current_page = None

        self.page_registry: Dict[str, Type[ctk.CTkFrame]] = {}

    def register(self, page_name, page_class):

        self.page_registry[page_name] = page_class

    def show(self, page_name):

        if page_name == self.current_page:
            return

        if page_name not in self.page_registry:
            return

        self.current_page = page_name

        self.app.clear_content()

        page = self.page_registry[page_name](

            self.app.content_frame

        )

        page.pack(

            fill="both",

            expand=True

        )

        self.app.sidebar.select(page_name)

        self.app.header.update_page(page_name)