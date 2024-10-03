import tkinter as tk
from tkinter import messagebox

class GameUI:
    def __init__(self, master, game_name):
        self.master = master
        self.master.title(game_name)
        self.master.geometry("400x300")

    def show_message(self, message):
        messagebox.showinfo("Resultado", message)

    def create_button(self, text, command):
        return tk.Button(self.master, text=text, command=command)

    def create_label(self, text):
        return tk.Label(self.master, text=text)

    def create_entry(self):
        return tk.Entry(self.master)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()
