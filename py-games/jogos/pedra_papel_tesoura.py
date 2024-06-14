import os
import time
import random

def ganhou(user, pc):
    if (user == '1' and pc == 'Tesoura') or (user == '2' and pc == 'Pedra') or (user == '3' and pc == 'Papel'):
        return print('\n\t\tVocê ganhou!')
    
    elif (user == '1' and pc == 'Pedra') or (user == '2' and pc == 'Papel') or (user == '3' and pc == 'Tesoura'):
        return print('\n\t\tDeu empate!')
    
    return print('\n\t\tVocê perdeu!')


def pedra_papel_tesoura():
    
    os.system('cls')

    while True:
        os.system('cls')
        print('\n\nDigite sua escolha:\n')
        print('\t[1]\t~~ Pedra ~~\n')
        print('\t[2]\t~~ Papel ~~\n')
        print('\t[3]\t~~ Tesoura ~~\n')

        escolha_do_user = input()

        if escolha_do_user in ['1', '2', '3']:
            break

    escolha_do_pc = random.choice(['Pedra', 'Papel', 'Tesoura'])

    os.system('cls')
    
    print('Computador escolheu: ', escolha_do_pc)
    ganhou(escolha_do_user, escolha_do_pc)

    time.sleep(2) 

