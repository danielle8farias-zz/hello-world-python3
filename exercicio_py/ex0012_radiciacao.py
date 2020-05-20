'''
Usuário informa dois numeros inteiros, um para o radicando e outro para o índice da raiz.
'''

radicando = int(input('Digite um número inteiro para o radicando: '))
indice = int(input('Digite um número inteiro para o índice da raiz: '))

#calculando a raiz
#1/n é o inverso do expoente de n, por isso pode ser usado dessa forma como raiz
raiz = radicando ** (1/indice)
print(f'Resultado da radiciação: {raiz}')
print()

#importando módulo de raiz quadrada
from math import sqrt
raiz_quadr = sqrt(radicando)
print(f'Raiz quadrada: {raiz_quadr}')
print()
