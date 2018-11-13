'''
Crie cinco números aleatórios e armazenar numa tupla. Mostrar os números gerados
e indicar o menor e o maior deles.
'''
print('-'*50)
print('{: ^50}'.format('MAIOR E MENOR EM TUPLA'))
print('-'*50)
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10))
print('Sorteei os valores {}'.format(n))
print()
print('O maior valor é: {}'.format(max(n)))
print('O menor valor é: {}'.format(min(n)))
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
