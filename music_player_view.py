import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

window = tk.Tk()

window.title("Music Player")
window.geometry("1000x600")

style = ThemedStyle(window)
style.set_theme("scidgrey")

window.mainloop()
