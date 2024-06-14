import os
import time
import random

def inicializa_palavras_forca(escolha):
    
    facil = [
        "Casa",
        "Gato",
        "Mesa",
        "Bola",
        "Pato",
        "Livro",
        "Pente",
        "Flor",
        "Fogo",
        "Muro"
        ]

    medio = [
        "Escola",
        "Mercado",
        "Tijolo",
        "Jardim",
        "Sorvete",
        "Janelas",
        "Martelo",
        "Borboleta",
        "Abacaxi",
        "Cadeira"
    ]

    dificil = [
        "Helicóptero",
        "Hipopótamo",
        "Bibliotecário",
        "Extraordinário",
        "Paralelepípedo",
        "Pneumonia",
        "Otorrinolaringologista",
        "Inconstitucional",
        "Anticonstitucional",
        "Constitucionalista"
    ]

    match escolha:
        case '1':
            return facil, 10
        case '2':
            return medio, 8
        case '3':
            return dificil, 5

def atualiza_palavra(palavra, erros, letras_que_foram):
    print('Adivinhe a palavra:\n\n')
    print('\t\t\t\t'+palavra+'         ', erros, '\n\t\t Letras que já foram: ', letras_que_foram)

def troca(palavra, indice, guess):
    if indice < 0 or indice >= len(palavra):
        raise IndexError("Índice fora do intervalo da palavra.")
    return palavra[:indice] + guess + palavra[indice+1:]

def forca():
    
    os.system('cls')
    letras_que_foram = []
    while True:
        os.system('cls')
        print('\n\nSelecione uma dificuldade:\n')
        print('\t[1]\t~~ Fácil ~~\n')
        print('\t[2]\t~~ Médio ~~\n')
        print('\t[3]\t~~ Difícil ~~\n')

        escolha_do_user = input()

        if escolha_do_user in ['1', '2', '3']:
            break
    
    palavras_nivel, erros = inicializa_palavras_forca(escolha_do_user)
    palavra = random.choice(palavras_nivel).lower()
    tam_palavra = len(palavra)*'_'
    
    parada = True
    
    while parada == True:
        os.system('cls')
        atualiza_palavra(tam_palavra, erros, letras_que_foram)
        
        while True:
            guess = input('--> ').lower()
            if len(guess) == 1:
                break
        if guess in palavra:
            for letra in range(len(palavra)):
                if palavra[letra] == guess:
                    tam_palavra = troca(tam_palavra, letra, guess)
                    if guess not in letras_que_foram:
                        letras_que_foram.append(guess)
                    #erros -= 1
                if '_' not in tam_palavra:
                    atualiza_palavra(tam_palavra, erros, letras_que_foram)
                    
                    print('\n\t\tVocê Descobriu a Palavra !!!!')
                    time.sleep(4) 
                    
                    parada = False
                    break
        else:
            print('Letra não está presente!')
            if guess not in letras_que_foram:
                letras_que_foram.append(guess)
            erros -= 1
            if erros == 0:
                parada = False
                atualiza_palavra(palavra, erros, letras_que_foram)
                print('\n\t\tVocê Perdeu!')
                time.sleep(4) 
                break
            time.sleep(1)
        
        