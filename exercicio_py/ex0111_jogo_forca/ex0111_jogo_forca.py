#!/usr/bin/env python3.8

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta

from interface import escolher_tema
from manipular_arquivos import abrir_temas

from time import sleep

jogando = True

while jogando:
    ler_cabecalho('jogo da forca')
    temas = abrir_temas()
    opcao = escolher_tema(temas)

    if opcao == 1:
        sleep(0.5)
        print(f'O tema escolhido foi: {temas[opcao - 1].upper()}')
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
