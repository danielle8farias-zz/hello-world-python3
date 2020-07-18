#!/usr/bin/env python3.8

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta

from interface import escolher_tema, desenhar_forca
from manipular_arquivos import abrir_temas

from time import sleep

################################################################

from random import choice
def tema_frutas(lista_frutas):
    fruta_escolhida = choice(lista_frutas)
    print(fruta_escolhida)
    return fruta_escolhida, len(fruta_escolhida)

def local_palavra(tamanho):
    string_oculta = '__ '*tamanho
    return string_oculta

def adivinhar_palavra(tamanho, palavra_oculta, fruta_escolhida):
    tentativas = 6
    while tentativas != 0:
        letra_escolhida = input('Escolha uma letra: ') #fazer o tratamento dessa entrada de dados
        if letra_escolhida in fruta_escolhida:
            pass


###################################################################

jogando = True

while jogando:
    ler_cabecalho('jogo da forca')
    temas = abrir_temas()
    opcao = escolher_tema(temas)

    if opcao == 1:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1].upper()}')
        #desenhar_forca()
        lista_frutas = ['uva', 'abacaxi', 'morango', 'kiwi', 'banana', 'abacate', 'laranja', 'limão', 'tangerina']
        fruta_escolhida, tamanho = tema_frutas(lista_frutas)
        palavra_oculta = local_palavra(tamanho)
        print(palavra_oculta)


    elif opcao == 2:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1].upper()}')
    elif opcao == 3:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1].upper()}')
    elif opcao == 4:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1].upper()}')
    elif opcao == 5:
        sleep(0.5)
        print('Finalizando o jogo')
        sleep(0.5)
        rodape()
        sleep(0.5)
        jogando = False
    else:
        print('Escolha uma opção válida!')
