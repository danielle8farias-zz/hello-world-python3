#!/usr/bin/env python3.8

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita dois números inteiros e programa retorna a soma entre eles.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_float

ler_cabecalho('somar')

while True:
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    print(f'\n{num1} + {num2} = {num1 + num2}')
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('\nDeseja rodar o programa de novo? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()
