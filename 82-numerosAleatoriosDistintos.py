'''
Gere uma lista de 15 números inteiros aleatórios entre 10 e 100 que sejam distintos entre si.
'''
print('-'*50)
print(f'{"SORTEIO DE 15 NÚMEROS ALEATÓRIOS":^50}')
print('-'*50)
from random import randint
lista = []
while len(lista) < 15:
    n = randint(10, 100)
    if n not in lista:
        lista.append(n)
lista.sort()
print(f'Seus números são:')
print(lista)
print('-'*50)
print(f'{"FIM":^50}')
print('-'*50)