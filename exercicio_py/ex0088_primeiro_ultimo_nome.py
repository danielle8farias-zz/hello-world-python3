#!/usr/bin/env python3.8

'''
Usuário informa nome completo e programa retorne apenas o primeiro e o último nome.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta, ler_palavra


ler_cabecalho('Retornando o primeiro e último nome')
while True:
    nome = ler_palavra('Digite seu nome completo: ')
    #split() transforma a string em lista, separando pelos espaços digitados
    n = nome.split()
    #[0] pegando o primeiro item da lista
    print(f'Seu primeiro nome é: {n[0]}')
    #[-1] pegando o último item da lista
    print(f'Seu último nome é: {n[-1]}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
rodape()
