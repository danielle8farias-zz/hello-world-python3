#!/usr/bin/env python3.8

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta

from interface import escolher_tema, desenhar_forca
from manipular_arquivos import abrir_arquivo

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
    erros = 0
    forca = desenhar_forca()
    lista_chutes = []
    lista_palavra_oculta = palavra_oculta.split()
    nova_palavra1 = ' '
    print(forca[erros])
    while (erros < 6) and (fruta_escolhida != nova_palavra1):
        chute = input('Escolha uma letra: ') #fazer o tratamento dessa entrada de dados
        posicao = 0

        if chute not in lista_chutes:
            lista_chutes.append(chute)
            print(lista_chutes)

            if chute not in fruta_escolhida:
                erros += 1
                print(f'Você tem {erros} erros.')
                print(forca[erros])
            else:
                for letra in fruta_escolhida:
                    if chute == letra:
                        print(f'letra: {chute.upper()}, na posição: {posicao}')
                        lista_palavra_oculta[posicao] = chute.upper()
                    posicao += 1
                nova_palavra = ' '.join(lista_palavra_oculta)
                nova_palavra1 = ''.join(lista_palavra_oculta).lower()
                print(nova_palavra)
                print(nova_palavra1)

        else:
            print('Essa letra já foi escolhida! Por favor, escolha outra.')

###################################################################

jogando = True

while jogando:
    ler_cabecalho('jogo da forca')
    temas = abrir_arquivo('temas.txt')
    opcao = escolher_tema(temas)

    if opcao == 1:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1].upper()}')
        lista_frutas = abrir_arquivo('frutas.txt')
        fruta_escolhida, tamanho = tema_frutas(lista_frutas)
        palavra_oculta = local_palavra(tamanho)
        print(palavra_oculta)
        adivinhar_palavra(tamanho, palavra_oculta, fruta_escolhida)


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
