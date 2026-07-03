import customtkinter as ctk
from tkinter import ttk
from typing import List, Dict, Any

from config.theme import CARD, BACKGROUND, TEXT, TEXT_SECONDARY


class PerformersTable(ctk.CTkFrame):
    """Table for top performing QR codes."""

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )

        self.data = []
        self.create_widgets()

    def create_widgets(self) -> None:
        title = ctk.CTkLabel(
            self,
            text="Top QR Codes",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        table_frame = ctk.CTkFrame(self, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(
            "Treeview",
            background=BACKGROUND,
            foreground=TEXT,
            fieldbackground=CARD,
            rowheight=28,
        )
        style.configure(
            "Treeview.Heading",
            background="#334155",
            foreground=TEXT,
            font=("Segoe UI", 10, "bold"),
        )
        style.map('Treeview', background=[('selected', '#334155')])

        columns = ("ID", "Type", "Data", "Scans", "Exports", "Created")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            height=10,
            show="headings",
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="w")

        self.tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscroll=scrollbar.set)

    def update_data(self, data: List[Dict[str, Any]]) -> None:
        """Update table with performer data."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in data:
            self.tree.insert(
                "",
                "end",
                values=(
                    row.get("id", ""),
                    row.get("type", ""),
                    row.get("value", ""),
                    row.get("scans", 0),
                    row.get("exports", 0),
                    row.get("created_at", ""),
                ),
            )

        self.data = data
