import tkinter as tk
from tkinter import messagebox

class GameUI:
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.is_dark_mode = False
        self.setup_theme()
        self.create_dark_mode_button()

    def setup_theme(self):
        self.light_theme = {
            'bg': 'white',
            'fg': 'black',
            'button': 'lightgray'
        }
        self.dark_theme = {
            'bg': 'black',
            'fg': 'white',
            'button': 'darkgray'
        }
        self.apply_theme()

    def apply_theme(self):
        theme = self.dark_theme if self.is_dark_mode else self.light_theme
        self.master.configure(bg=theme['bg'])
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=theme['button'], fg=theme['fg'])
            else:
                widget.configure(bg=theme['bg'], fg=theme['fg'])

    def create_dark_mode_button(self):
        button = tk.Button(self.master, text='', width=2, height=1, command=self.toggle_dark_mode)
        button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def toggle_dark_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

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
