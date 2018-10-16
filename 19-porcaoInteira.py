'''
Leia um número real qualquer e retorne apenas a parte inteira.
'''
print('-'*50)
print('{: ^50}'.format('PARTE INTEIRA DE UM NÚMERO REAL'))
print('-'*50)
from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira do valor digitado foi {}.'.format(trunc(num)))
