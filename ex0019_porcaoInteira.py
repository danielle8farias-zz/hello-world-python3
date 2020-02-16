#!/usr/bin/env python3.7
'''
Leia um número real qualquer e retorne apenas a parte inteira,
sem arredondamento.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from math import trunc

#programa principal
cabecalho('PARTE INTEIRA DE UM NÚMERO REAL')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = float(input('Digite um número real: '))
    print(f'A parte inteira do valor digitado foi {trunc(num)}.')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
