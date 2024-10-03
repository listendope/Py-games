import tkinter as tk
from jogos.forca import forca
from jogos.jogo_da_velha import jogo_da_velha
from jogos.pedra_papel_tesoura import pedra_papel_tesoura
from jogos.game_ui import GameUI

class MainUI(GameUI):
    def __init__(self, master):
        super().__init__(master, "Py-Games")
        self.games = {
            'Jogo da Velha': jogo_da_velha,
            'Pedra Papel ou Tesoura': pedra_papel_tesoura,
            'Forca': forca
        }
        self.setup_main_menu()

    def setup_main_menu(self):
        self.clear_window()
        self.create_label("Escolha qual jogo quer jogar:").pack(pady=10)
        for game_name, game_func in self.games.items():
            self.create_button(game_name, lambda g=game_func: self.play_game(g)).pack(pady=5)
        self.create_button("Sair", self.quit_game).pack(pady=10)
        self.create_theme_button()

    def create_theme_button(self):
        theme_button = tk.Button(self.master, text="🌓", command=self.toggle_theme, width=2, height=1)
        theme_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
        
    def play_game(self, game_func):
        self.master.withdraw()
        game_func()
        self.master.deiconify()

    def quit_game(self):
        self.master.quit()  # Stop the mainloop
        self.master.destroy()  # Destroy the main window
        exit()  # Exit the Python interpreter

def main():
    root = tk.Tk()
    game = MainUI(root)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 400
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()
