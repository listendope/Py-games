import os
import time
from jogos.pedra_papel_tesoura import *
from jogos.forca import *
from jogos.jogo_da_velha import *

def main():
    
    while True:
        os.system('cls')

        print('\n\nEscolha qual jogo quer jogar:\n')
        print('1 - Jogo da Velha')
        print('2 - Pedra Papel ou Tesoura')
        print('3 - Forca\n')
        print('[APERTE OUTRA TECLA PARA FINALIZAR]\n')
        
        opcao = input()
        
        match opcao:
            case '1':
                jogo_da_velha()
            
            case '2':
                pedra_papel_tesoura()
            
            case '3':
                forca()
            
            case _:
                os.system('cls')
                print('\n\nSaindo ...\n\n')
                break
            
    
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    
    print('\n\nObrigado por Jogar!\n\n')

            
if __name__ == "__main__":
    main()





















main()