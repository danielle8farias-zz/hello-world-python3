#!/usr/bin/env python3.8

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape

from interface import escolher_tema, desenhar_forca
from manipular_arquivos import abrir_arquivo
from palavra_pc import escolher_palavra, palavra_secreta, adivinhar_palavra

from time import sleep


jogando = True

while jogando:
    ler_cabecalho('jogo da forca')
    #abrindo arquivo de temas
    temas = abrir_arquivo('temas.txt')
    opcao = escolher_tema(temas)
    #frutas
    if opcao == 1:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1]}')
        #abrindo arquivo com nome de frutas
        lista_frutas = abrir_arquivo('frutas.txt')
        #recebendo retorno de palavra escolhida e tamanho
        fruta_escolhida, tamanho = escolher_palavra(lista_frutas)
        #recebendo retorno de palavra secreta
        palavra_oculta = palavra_secreta(tamanho)

        adivinhar_palavra(tamanho, palavra_oculta, fruta_escolhida)


    elif opcao == 2:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1]}')
    elif opcao == 3:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1]}')
    elif opcao == 4:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1]}')
    elif opcao == 5:
        sleep(0.5)
        print('Finalizando o jogo')
        sleep(0.5)
        rodape()
        sleep(0.5)
        jogando = False
    else:
        print('Escolha uma opção válida!')
