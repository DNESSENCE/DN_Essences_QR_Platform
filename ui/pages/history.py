import customtkinter as ctk

from config.theme import PRIMARY
from controllers.history_controller import HistoryController
from ui.components.history_filters import HistoryFilters
from ui.components.history_toolbar import HistoryToolbar
from ui.components.history_table import HistoryTable


class HistoryPage(ctk.CTkFrame):
    """Professional history page for QR code management."""

    def __init__(self, master):
        super().__init__(master, fg_color=PRIMARY)

        self.controller = None
        self.table = None
        self.filters = None
        self.toolbar = None

        self.create_layout()

    def create_layout(self) -> None:
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 5))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="QR Code History",
            font=("Segoe UI", 28, "bold"),
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Manage and track all your QR codes",
            font=("Segoe UI", 13),
        )
        subtitle.pack(anchor="w")

        self.filters = HistoryFilters(self)
        self.filters.grid(row=1, column=0, sticky="ew", padx=15, pady=10)

        self.table = HistoryTable(self, on_row_select=self._on_row_select)
        self.table.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 10))

        self.toolbar = HistoryToolbar(self)
        self.toolbar.grid(row=3, column=0, sticky="ew", padx=15, pady=(0, 15))

        self.controller = HistoryController(self)
        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self.filters.set_search_callback(self._on_search)
        self.filters.set_type_filter_callback(self._on_type_filter)

        self.toolbar.set_duplicate_callback(self._on_duplicate)
        self.toolbar.set_delete_callback(self._on_delete)
        self.toolbar.set_restore_callback(self._on_restore)
        self.toolbar.set_export_callback(self._on_export)
        self.toolbar.set_refresh_callback(self._on_refresh)

    def _on_row_select(self, qr_id: str) -> None:
        self.controller.select_qr(qr_id)

    def _on_search(self, query: str) -> None:
        self.controller.search(query)

    def _on_type_filter(self, qr_type: str) -> None:
        self.controller.filter_by_type(qr_type)

    def _on_duplicate(self) -> None:
        qr_id = self.table.get_selected()
        if qr_id:
            self.controller.duplicate_qr(qr_id)

    def _on_delete(self) -> None:
        qr_id = self.table.get_selected()
        if qr_id:
            self.controller.delete_qr(qr_id)

    def _on_restore(self) -> None:
        qr_id = self.table.get_selected()
        if qr_id:
            self.controller.restore_qr(qr_id)

    def _on_export(self) -> None:
        qr_id = self.table.get_selected()
        if qr_id:
            self.controller.export_qr(qr_id)

    def _on_refresh(self) -> None:
        self.controller.refresh()