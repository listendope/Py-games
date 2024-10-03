import random
from .game_ui import GameUI
import tkinter as tk

class PedraPapelTesouraUI(GameUI):
    def __init__(self, master):
        super().__init__(master, "Pedra Papel Tesoura")
        self.choices = ['Pedra', 'Papel', 'Tesoura']
        self.setup_game()

    def setup_game(self):
        self.clear_window()
        self.create_label("Faça sua escolha:").pack(pady=10)
        for choice in self.choices:
            self.create_button(choice, lambda c=choice: self.play(c)).pack(pady=5)

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)
        self.show_message(f"Você escolheu: {player_choice}\nComputador escolheu: {computer_choice}\n\n{result}")
        self.setup_game()

    def determine_winner(self, player, computer):
        if player == computer:
            return "Empate!"
        elif ((player == 'Pedra' and computer == 'Tesoura') or
              (player == 'Papel' and computer == 'Pedra') or
              (player == 'Tesoura' and computer == 'Papel')):
            return "Você ganhou!"
        else:
            return "Você perdeu!"

def pedra_papel_tesoura():
    root = tk.Tk()
    game = PedraPapelTesouraUI(root)
    root.mainloop()
