import os
import time
from jogos import pedra_papel_tesoura, forca, jogo_da_velha

GAMES = {
    '1': ('Jogo da Velha', jogo_da_velha.jogo_da_velha),
    '2': ('Pedra Papel ou Tesoura', pedra_papel_tesoura.pedra_papel_tesoura),
    '3': ('Forca', forca.forca)
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print('\n\nEscolha qual jogo quer jogar:\n')
    for key, (game_name, _) in GAMES.items():
        print(f'{key} - {game_name}')
    print('\n[APERTE OUTRA TECLA PARA FINALIZAR]\n')

def main():
    while True:
        clear_screen()
        display_menu()
        
        opcao = input()
        
        if opcao in GAMES:
            GAMES[opcao][1]()
        else:
            clear_screen()
            print('\n\nSaindo ...\n\n')
            break
    
    time.sleep(1)
    clear_screen()
    time.sleep(1)
    
    print('\n\nObrigado por Jogar!\n\n')

if __name__ == "__main__":
    main()
