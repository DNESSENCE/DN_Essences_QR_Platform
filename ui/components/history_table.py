import customtkinter as ctk
from tkinter import ttk
from typing import List, Callable, Optional

from config.theme import CARD, PRIMARY


class HistoryTable(ctk.CTkFrame):
    """Professional table component for displaying QR history."""

    def __init__(self, master, on_row_select: Optional[Callable] = None):
        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color="#334155",
        )

        self.on_row_select = on_row_select
        self.selected_row = None
        self.create_widgets()

    def create_widgets(self) -> None:
        title = ctk.CTkLabel(
            self,
            text="QR Code History",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        table_frame = ctk.CTkFrame(self, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#1E293B", foreground="#FFFFFF", fieldbackground="#273549")
        style.configure("Treeview.Heading", background="#334155", foreground="#FFFFFF")

        columns = ("ID", "Type", "Data", "Scans", "Exports", "Created")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            height=15,
            show="headings",
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<ButtonRelease-1>", self._on_select)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

    def update_data(self, data: List[tuple]) -> None:
        """Update the table with new data."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in data:
            self.tree.insert("", "end", values=row)

    def get_selected(self) -> Optional[str]:
        """Get the selected row ID."""
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0])["values"][0]
        return None

    def _on_select(self, event) -> None:
        """Handle row selection."""
        self.selected_row = self.get_selected()
        if self.on_row_select and self.selected_row:
            self.on_row_select(self.selected_row)
