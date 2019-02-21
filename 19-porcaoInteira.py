'''
Leia um número real qualquer e retorne apenas a parte inteira,
sem arredondamento.
'''
from mensagem import cabecalho
from mensagem import rodape
from math import trunc

cabecalho('PARTE INTEIRA DE UM NÚMERO REAL')

while True:
    num = float(input('Digite um número real: '))
    print('A parte inteira do valor digitado foi {}.'.format(trunc(num)))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
