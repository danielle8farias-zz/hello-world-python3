'''
Crie cinco números aleatórios e armazenar numa tupla. Mostrar os números gerados
e indicar o menor e o maior deles.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('MAIOR E MENOR EM TUPLA')

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10))
print('Sorteei os valores {}'.format(n))
print()
print('O maior valor é: {}'.format(max(n)))
print('O menor valor é: {}'.format(min(n)))

rodape()
