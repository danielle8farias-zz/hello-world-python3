#!/usr/bin/env python3.8

'''
Usuário informa um número inteiro e escolhe uma opção de conversão desse número. O programa retorna a conversão escolhida desse número para base binária, octal ou hexadecimal.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_int, ler_num_nat


def f_escolha(opcao):
    if opcao == 1:
        #bin() convertendo para binário
        print(f'Em binário: {bin(num)[2:]}')
    elif opcao == 2:
        print(f'Em octal: {oct(num)[2:]}')
    elif opcao == 3:
        print(f'Em hexadecimal: {hex(num)[2:]}')
    else:
        print('Opção inválida!')


#programa principal
ler_cabecalho('BASES BINÁRIA, OCTAL E HEXADECIMAL')
while True:
    num = ler_num_int('Digite um número inteiro: ')
    print('''Escolha a base para conversão:
    [1] binário
    [2] octal
    [3] hexadecimal''')
    opcao = ler_num_nat('Sua opção: ')
    f_escolha(opcao)
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
rodape()
