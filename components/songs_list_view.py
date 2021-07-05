import tkinter as tk

class SongsListView(tk.Frame, database):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, height = 600, width = 400)
        self.parent = parent
        self.database = database
        self.list_view = tk.ListBox(tk.Frame)