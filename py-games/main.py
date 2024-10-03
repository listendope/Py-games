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
        self.create_button("Sair", self.master.quit).pack(pady=10)

    def play_game(self, game_func):
        self.master.withdraw()
        game_func()
        self.master.deiconify()

def main():
    root = tk.Tk()
    game = MainUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
