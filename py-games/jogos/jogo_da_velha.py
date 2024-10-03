from .game_ui import GameUI
import tkinter as tk

class JogoDaVelhaUI(GameUI):
    def __init__(self, master):
        super().__init__(master, "Jogo da Velha")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.setup_game()

    def setup_game(self):
        self.clear_window()
        for i in range(9):
            button = self.create_button(self.board[i], lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3, sticky="nsew")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.setup_game()
            if self.check_winner():
                self.show_message(f"Jogador {self.current_player} venceu!")
                self.reset_game()
            elif ' ' not in self.board:
                self.show_message("Empate!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]
        return any(self.board[i] == self.board[j] == self.board[k] != ' '
                   for i, j, k in winning_combinations)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.setup_game()

def jogo_da_velha():
    root = tk.Tk()
    game = JogoDaVelhaUI(root)
    root.mainloop()
