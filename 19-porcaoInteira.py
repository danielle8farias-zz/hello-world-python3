'''
Leia um número real qualquer e retorne apenas a parte inteira,
sem arredondamento.
'''
print('-'*50)
print('{: ^50}'.format('PARTE INTEIRA DE UM NÚMERO REAL'))
print('-'*50)
from math import trunc
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
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
