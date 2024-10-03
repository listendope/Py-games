import random
from .game_ui import GameUI
import tkinter as tk

class ForcaUI(GameUI):
    def __init__(self, master):
        super().__init__(master, "Forca")
        self.palavras = {
            'Fácil': [
                "Casa", "Gato", "Mesa", "Bola", "Pato", "Livro", "Pente", "Flor",
                "Fogo", "Muro", "Rato", "Cama", "Vaso", "Pena", "Roda", "Sopa",
                "Lupa", "Rede", "Tela", "Cubo", "Faca", "Lobo", "Anel", "Pipa"
            ],
            'Médio': [
                "Escola", "Barraca", "Mercado", "Tijolo", "Jardim", "Sorvete",
                "Janelas", "Martelo", "Borboleta", "Abacaxi", "Cadeira", "Telefone",
                "Bicicleta", "Guitarra", "Cachorro", "Elefante", "Computador",
                "Chocolate", "Montanha", "Oceano", "Foguete", "Pintura", "Relógio",
                "Tesoura"
            ],
            'Difícil': [
                "Helicóptero", "Hipopótamo", "Bibliotecário", "Extraordinário",
                "Paralelepípedo", "Pneumonia", "Otorrinolaringologista",
                "Inconstitucional", "Anticonstitucional", "Constitucionalista",
                "Interdisciplinaridade", "Fotossíntese", "Eletrocardiograma",
                "Biodiversidade", "Sustentabilidade", "Nanotecnologia",
                "Epistemologia", "Procrastinação", "Idiossincrasia", "Paradigma"
            ]
        }
        self.setup_difficulty_selection()

    def setup_difficulty_selection(self):
        self.clear_window()
        self.create_label("Selecione uma dificuldade:").pack(pady=10)
        for difficulty in self.palavras.keys():
            self.create_button(difficulty, lambda d=difficulty: self.start_game(d)).pack(pady=5)
        
        # Add the button to return to the main menu
        self.create_button("Voltar ao Menu Principal", self.return_to_main_menu).pack(pady=40)
        self.create_theme_button()

    def create_theme_button(self):
        theme_button = tk.Button(self.master, text="🌓", command=self.toggle_theme, width=2, height=1)
        theme_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
        
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
                self.show_message(f"Parabéns! Você ganhou! A palavra é: {self.palavra}")
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
    
    def return_to_main_menu(self):
        self.master.destroy()
        from main import main
        main()

def forca():
    root = tk.Tk()
    game = ForcaUI(root)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 400
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    root.mainloop()
