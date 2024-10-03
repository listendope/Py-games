import random
from .game_ui import GameUI
import tkinter as tk

class ForcaUI(GameUI):
    def __init__(self, master):
        super().__init__(master, "Forca")
        self.palavras = {
            'Fácil': ["Casa", "Gato", "Mesa", "Bola", "Pato"],
            'Médio': ["Escola", "Barraca", "Mercado", "Tijolo", "Jardim"],
            'Difícil': ["Helicóptero", "Hipopótamo", "Bibliotecário", "Extraordinário", "Paralelepípedo"]
        }
        self.setup_difficulty_selection()

    def setup_difficulty_selection(self):
        self.clear_window()
        self.create_label("Selecione uma dificuldade:").pack(pady=10)
        for difficulty in self.palavras.keys():
            self.create_button(difficulty, lambda d=difficulty: self.start_game(d)).pack(pady=5)

    def start_game(self, difficulty):
        self.palavra = random.choice(self.palavras[difficulty]).lower()
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas = 6
        self.update_game_ui()

    def update_game_ui(self):
        self.clear_window()
        palavra_atual = ''.join(letra if letra in self.letras_corretas else '_' for letra in self.palavra)
        self.create_label(f"Palavra: {palavra_atual}").pack(pady=10)
        self.create_label(f"Letras erradas: {', '.join(self.letras_erradas)}").pack()
        self.create_label(f"Tentativas restantes: {self.tentativas}").pack()
        
        entry = self.create_entry()
        entry.pack(pady=10)
        self.create_button("Adivinhar", lambda: self.guess(entry.get().lower())).pack()

    def guess(self, letra):
        if letra in self.palavra:
            self.letras_corretas.add(letra)
            if set(self.palavra) == self.letras_corretas:
                self.show_message("Parabéns! Você ganhou!")
                self.setup_difficulty_selection()
                return
        else:
            self.letras_erradas.add(letra)
            self.tentativas -= 1
            if self.tentativas == 0:
                self.show_message(f"Você perdeu! A palavra era: {self.palavra}")
                self.setup_difficulty_selection()
                return
        self.update_game_ui()

def forca():
    root = tk.Tk()
    game = ForcaUI(root)
    root.mainloop()
