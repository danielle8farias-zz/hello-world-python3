#!/usr/bin/env python3.8

'''
Usuário digita uma palavra ou frase, e programa retorna a mesma com as vogais trocadas por *(asterisco).
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta, ler_palavra


ler_cabecalho('TROCA VOGAIS POR ASTERÍSCO')
while True:
    palavra = ler_palavra('Escreva uma palavra ou frase: ').lower()
    troca = ''
    for letra in range(len(palavra)):
        if palavra[letra] in 'aeiou':
            troca += '*'
        else:
            troca += palavra[letra]
    print(f'A nova palavra é: {troca}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
    print()
rodape()
