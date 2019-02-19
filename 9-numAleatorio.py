'''
Mostrando um número aleatório entre 0 e 1.
E outro número aleatório entre 1 e 10.
'''
from mensagem import cabecalho
from mensagem import rodape
import random

cabecalho('NÚMEROS ALEATÓRIOS')

while True:
    num = random.random()
    num2 = random.randint(1,10)
    print('Primeiro número aleatório entre 0 e 1')
    print(num)
    print('Segundo número aleatório entre 1 e 10')
    print(num2)
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
