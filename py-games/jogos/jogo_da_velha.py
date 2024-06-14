import os
import time
import random

def inicializa_mapa():
    mapa = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]
    lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    return mapa, lista

def atualiza_board(mapa):
    print('\t\t\t'+' '+mapa[0][0]+' '+'| '+' '+mapa[0][1]+' '+'| '+' '+mapa[0][2]+' ')
    print('\n\t\t\t____________\n')
    print('\t\t\t'+' '+mapa[1][0]+' '+'| '+' '+mapa[1][1]+' '+'| '+' '+mapa[1][2]+' ')
    print('\n\t\t\t____________\n')
    print('\t\t\t'+' '+mapa[2][0]+' '+'| '+' '+mapa[2][1]+' '+'| '+' '+mapa[2][2]+' ')

def faz_jogada(mapa, jogada, lista):
   if jogada in lista:
        match jogada:
            case '7':
                mapa[0][0] = 'X'
                lista.remove('7')
            case '8':
                mapa[0][1] = 'X'
                lista.remove('8')
            case '9':
                mapa[0][2] = 'X'
                lista.remove('9')
            case '4':
                mapa[1][0] = 'X'
                lista.remove('4')
            case '5':
                mapa[1][1] = 'X'
                lista.remove('5')
            case '6':
                mapa[1][2] = 'X'
                lista.remove('6')
            case '1':
                mapa[2][0] = 'X'
                lista.remove('1')
            case '2':
                mapa[2][1] = 'X'
                lista.remove('2')
            case '3':
                mapa[2][2] = 'X'
                lista.remove('3')
        return 'continua'
   return 'refaz'
       
def jogada_pc(mapa, lista):
    escolha_do_pc = random.choice(lista)
    match escolha_do_pc:
            case '7':
                mapa[0][0] = 'O'
                lista.remove('7')
            case '8':
                mapa[0][1] = 'O'
                lista.remove('8')
            case '9':
                mapa[0][2] = 'O'
                lista.remove('9')
            case '4':
                mapa[1][0] = 'O'
                lista.remove('4')
            case '5':
                mapa[1][1] = 'O'
                lista.remove('5')
            case '6':
                mapa[1][2] = 'O'
                lista.remove('6')
            case '1':
                mapa[2][0] = 'O'
                lista.remove('1')
            case '2':
                mapa[2][1] = 'O'
                lista.remove('2')
            case '3':
                mapa[2][2] = 'O'
                lista.remove('3')
    
def valida_se_ganhou(mapa):
    if(mapa[0][0] == 'X' and mapa[0][1] == 'X' and mapa[0][2] == 'X') or (mapa[1][0] == 'X' and mapa[1][1] == 'X' and mapa[1][2] == 'X') or (mapa[2][0] == 'X' and mapa[2][1] == 'X' and mapa[2][2] == 'X') or (mapa[1][0] == 'X' and mapa[0][0] == 'X' and mapa[2][0] == 'X') or (mapa[0][1] == 'X' and mapa[1][1] == 'X' and mapa[2][1] == 'X') or (mapa[0][2] == 'X' and mapa[2][2] == 'X' and mapa[1][2] == 'X') or (mapa[1][0] == 'X' and mapa[0][0] == 'X' and mapa[2][0] == 'X') or (mapa[0][1] == 'X' and mapa[1][1] == 'X' and mapa[2][1] == 'X') or (mapa[0][0] == 'X' and mapa[2][2] == 'X' and mapa[1][1] == 'X') or (mapa[1][0] == 'X' and mapa[0][0] == 'X' and mapa[2][0] == 'X') or (mapa[0][1] == 'X' and mapa[1][1] == 'X' and mapa[2][1] == 'X') or (mapa[0][2] == 'X' and mapa[2][0] == 'X' and mapa[1][1] == 'X'):
        return '\nVocê ganhou!'
    elif (mapa[0][0] == 'O' and mapa[0][1] == 'O' and mapa[0][2] == 'O') or (mapa[1][0] == 'O' and mapa[1][1] == 'O' and mapa[1][2] == 'O') or (mapa[2][0] == 'O' and mapa[2][1] == 'O' and mapa[2][2] == 'O') or (mapa[1][0] == 'O' and mapa[0][0] == 'O' and mapa[2][0] == 'O') or (mapa[0][1] == 'O' and mapa[1][1] == 'O' and mapa[2][1] == 'O') or (mapa[0][2] == 'O' and mapa[2][2] == 'O' and mapa[1][2] == 'O') or (mapa[1][0] == 'O' and mapa[0][0] == 'O' and mapa[2][0] == 'O') or (mapa[0][1] == 'O' and mapa[1][1] == 'O' and mapa[2][1] == 'O') or (mapa[0][0] == 'O' and mapa[2][2] == 'O' and mapa[1][1] == 'O') or (mapa[1][0] == 'O' and mapa[0][0] == 'O' and mapa[2][0] == 'O') or (mapa[0][1] == 'O' and mapa[1][1] == 'O' and mapa[2][1] == 'O') or (mapa[0][2] == 'O' and mapa[2][0] == 'O' and mapa[1][1] == 'O'):
        return '\nComputador ganhou!'
    return False
        
def jogo_da_velha():
    
    os.system('cls')
    mapa, lista_posicoes = inicializa_mapa()

    print('Com o auxílio do teclado numérico, selecione onde quer jogar considerando as regras abaixo: \n')
    print('\t\t\t'+' '+'7'+' '+'| '+' '+'8'+' '+'| '+' '+'9'+' ')
    print('\n\t\t\t____________\n')
    print('\t\t\t'+' '+'4'+' '+'| '+' '+'5'+' '+'| '+' '+'6'+' ')
    print('\n\t\t\t____________\n')
    print('\t\t\t'+' '+'1'+' '+'| '+' '+'2'+' '+'| '+' '+'3'+' ')
    
    time.sleep(7)  

    while True:
        os.system('cls')
        
        print('\t\t\tEscolha uma posição: \n\n')
        atualiza_board(mapa)
        
        jogada = input('--> ')
        
        while True:
            valida = faz_jogada(mapa, jogada, lista_posicoes)
            if valida != 'refaz':
                break
            jogada = input('--> ')

        valida = valida_se_ganhou(mapa)
        if valida != False:
            atualiza_board(mapa)
            print(valida)
            break
        
        if len(lista_posicoes) != 0:
            print('Computador jogando . . .')
            time.sleep(2)
            jogada_pc(mapa, lista_posicoes)
            atualiza_board(mapa)
            valida = valida_se_ganhou(mapa)
            if valida != False:
                print(valida)
                break
        else:
            os.system('cls')
            atualiza_board(mapa)
            print('\nDeu velha !!')
            break
        
    time.sleep(5)