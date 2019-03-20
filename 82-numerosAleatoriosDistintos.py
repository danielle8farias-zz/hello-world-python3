'''
Gere uma lista de 15 números inteiros aleatórios entre 10 e 100 que sejam distintos entre si.
'''
from mensagem import cabecalho
from mensagem import rodape
from random import randint

cabecalho('SORTEIO DE 15 NÚMEROS ALEATÓRIOS')

lista = []
while len(lista) < 15:
    n = randint(10, 100)
    if n not in lista:
        lista.append(n)
lista.sort()
print(f'Seus números são:')
print(lista)

rodape()
