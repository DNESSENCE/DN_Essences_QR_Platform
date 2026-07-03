import customtkinter as ctk
from tkinter import ttk, messagebox
from typing import List, Dict, Any

from config.theme import PRIMARY, CARD, TEXT, TEXT_SECONDARY


class ProductsPage(ctk.CTkFrame):
    """Products management placeholder for future updates."""

    def __init__(self, master):
        super().__init__(master, fg_color=PRIMARY)

        self.controller = None
        self.table = None
        self.create_layout()

    def create_layout(self) -> None:
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 5))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(header, text="Products", font=("Segoe UI", 28, "bold"))
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(header, text="Manage product catalog (placeholder)", font=("Segoe UI", 12), text_color=TEXT_SECONDARY)
        subtitle.pack(anchor="w")

        action_frame = ctk.CTkFrame(self, fg_color="transparent")
        action_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=(8, 10))
        action_frame.grid_columnconfigure(2, weight=1)

        add_btn = ctk.CTkButton(action_frame, text="Add Product", width=140, fg_color="#16A34A")
        add_btn.grid(row=0, column=0, padx=(0, 8))
        add_btn.configure(command=self._on_add)

        import_btn = ctk.CTkButton(action_frame, text="Import", width=100, fg_color="#374151")
        import_btn.grid(row=0, column=1, padx=(0, 8))
        import_btn.configure(command=self._on_import)

        search_entry = ctk.CTkEntry(action_frame, placeholder_text="Search products...")
        search_entry.grid(row=0, column=2, sticky="ew")
        search_entry.bind("<Return>", lambda e: self._on_search(search_entry.get()))

        table_frame = ctk.CTkFrame(self, fg_color="transparent")
        table_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure("Treeview", background=PRIMARY, fieldbackground=CARD, foreground=TEXT, rowheight=28)
        style.configure("Treeview.Heading", background="#334155", foreground=TEXT, font=("Segoe UI", 10, "bold"))

        columns = ("ID", "Name", "SKU", "Price", "Stock")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=140, anchor="w")

        self.table.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.table.configure(yscroll=scrollbar.set)

    def _on_add(self) -> None:
        messagebox.showinfo("Not implemented", "Add product will be available in a future update.")

    def _on_import(self) -> None:
        messagebox.showinfo("Not implemented", "Import products will be available in a future update.")

    def _on_search(self, query: str) -> None:
        messagebox.showinfo("Search", f"Search for: {query} (not implemented)")