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
        
        # Add the button to return to the main menu
        self.create_button("Voltar ao Menu Principal", self.return_to_main_menu).pack(pady=20)
        self.create_theme_button()

    def create_theme_button(self):
        theme_button = tk.Button(self.master, text="🌓", command=self.toggle_theme, width=2, height=1)
        theme_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
        
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

    def return_to_main_menu(self):
        self.master.destroy()
        from main import main
        main()

def pedra_papel_tesoura():
    root = tk.Tk()
    game = PedraPapelTesouraUI(root)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 400
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    root.mainloop()
