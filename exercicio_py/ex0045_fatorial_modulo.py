'''
Usuário informa um número inteiro e programa retorna o seu fatorial; usando o módulo.
'''

from math import factorial

num = int(input('Digite um número inteiro: '))

f = factorial(num)

print(f'Fatorial: {f}')
