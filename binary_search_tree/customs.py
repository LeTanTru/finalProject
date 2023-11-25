from tkinter import *
from variables import *


class HoverButton(Button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.config(bg="black", fg="white")

    def on_leave(self, event):
        self.config(bg="white", fg="black")
