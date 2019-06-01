'''
Mostrando um número aleatório entre 0 e 1.
E outro número aleatório entre 1 e 10.
'''
from mensagem import cabecalho
from mensagem import rodape
import random

#funções
def num_aleatorio1():
    num = random.random()
    return num

def num_aleatorio2():
    num = random.randint(1,10)
    return num

#programa principal
cabecalho('NÚMEROS ALEATÓRIOS')
while True:
    num1 = num_aleatorio1()
    num2 = num_aleatorio2()
    print('Primeiro número aleatório entre 0 e 1')
    print(num1)
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
