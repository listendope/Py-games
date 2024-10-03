from .game_ui import GameUI
import tkinter as tk
import random

class JogoDaVelhaUI(GameUI):
    def __init__(self, master):
        super().__init__(master, "Jogo da Velha")
        self.master.geometry("400x450")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.game_mode = None
        self.setup_mode_selection()

    def setup_mode_selection(self):
        self.clear_window()
        self.create_label("Escolha o modo de jogo:").pack(pady=10)
        self.create_button("Jogador vs Jogador", lambda: self.set_game_mode("PvP")).pack(pady=5)
        self.create_button("Jogador vs Computador", lambda: self.set_game_mode("PvC")).pack(pady=5)
        self.create_button("Voltar ao Menu Principal", self.return_to_main_menu).pack(pady=20)

    def set_game_mode(self, mode):
        self.game_mode = mode
        self.setup_game()

    def setup_game(self):
        self.clear_window()
        
        self.turn_label = self.create_label(f"Turno do Jogador {self.current_player}")
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                button = self.create_button(self.board[index], lambda idx=index: self.make_move(idx))
                button.config(width=10, height=3)
                button.grid(row=i+1, column=j, padx=2, pady=2)

        reset_button = self.create_button("Reiniciar", self.reset_game)
        reset_button.grid(row=4, column=0, columnspan=3, pady=10)

        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.master.grid_columnconfigure(j, weight=1)

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
                self.turn_label.config(text=f"Turno do Jogador {self.current_player}")
                if self.game_mode == "PvC" and self.current_player == 'O':
                    self.ai_move()

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.make_move(best_move)

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner():
            return 1 if is_maximizing else -1
        if ' ' not in board:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

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
        self.setup_mode_selection()

    def return_to_main_menu(self):
        self.master.destroy()
        from main import main
        main()

def jogo_da_velha():
    root = tk.Tk()
    game = JogoDaVelhaUI(root)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 400
    window_height = 450
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    root.mainloop()
