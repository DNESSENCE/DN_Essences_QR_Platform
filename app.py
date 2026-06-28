import customtkinter as ctk

from ui.layout.main_window import MainWindow

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def main():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()