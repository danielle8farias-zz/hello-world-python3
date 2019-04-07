'''
Faça um programa com uma lista de números inteiros e 2 funções; uma para sortear 5 números e
outra para somar os pares dessa lista.
'''
from mensagem import cabecalho
from mensagem import rodape
from random import randint
from time import sleep

cabecalho('sorteia e soma pares de uma lista')

def sorteia(lista):
    for i in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(.5)
    print()


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Soma dos nºs pares: {soma}')

while True:
    num = []
    print('Sorteando os números...')
    sorteia(num)
    somaPar(num)
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
