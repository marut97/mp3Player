import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from components.database import Database


class MusicPlayerApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.database = Database()
        parent.title("Music Player")
        parent.geometry("1000x600")

        style = ThemedStyle(parent)
        style.set_theme("scidgrey")


if __name__ == "__main__":
    window = tk.Tk()
    MusicPlayerApplication(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
