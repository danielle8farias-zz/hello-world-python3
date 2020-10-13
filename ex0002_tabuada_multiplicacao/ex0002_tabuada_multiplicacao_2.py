#!/usr/bin/env python3.8

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita dois números inteiros e programa retorna a tabuada de multiplicação desse.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_nat

ler_cabecalho('tabuada de multiplicação')

while True:
    num = ler_num_nat('Digite um número: ')
    i = 1
    for i in range(i, 10):
        print(f'{num:4} x {i} = {num*i}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('\nDeseja rodar o programa de novo? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()
