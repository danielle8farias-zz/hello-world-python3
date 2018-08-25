'''
Leia um número real qualquer e retorne apenas a parte inteira.
'''
from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira do valor digitado foi {}.'.format(trunc(num)))
