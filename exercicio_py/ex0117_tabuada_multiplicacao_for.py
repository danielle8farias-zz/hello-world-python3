#!/usr/bin/env python3.8

'''
Usuário fornece um número inteiro e programa retorna a tabuada de multiplicação desse. 
Com validação de dados.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
from numeros import ler_num_int

ler_cabecalho('tabuada de multiplicação')
while True:
    num = ler_num_int('Digite um número inteiro: ')
    print()
    for i in range (0,11):
        multiplicacao = num * i
        print(f'{num} x {i:2} = {multiplicacao}')
    print()
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    if resposta == 'N':
        break
    else:
        linha()
        print()
rodape()
