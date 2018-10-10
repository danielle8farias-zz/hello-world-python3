'''
Informe a raiz quadrada de um número inteiro.
'''
print('-'*50)
print('{: ^50}'.format('RAÍZ QUADRADA'))
print('-'*50)
from math import sqrt
num = int(input('digite um número inteiro: '))
raiz = sqrt(num)
print('A raiz de {} = {}'.format(num, raiz))
