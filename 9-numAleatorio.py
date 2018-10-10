'''
Mostrando um número aleatório entre 0 e 1.
E outro número aleatório entre 1 e 10.
'''
print('-'*50)
print('{: ^50}'.format('NÚMEROS ALEATÓRIOS'))
print('-'*50)
import random
num = random.random()
num2 = random.randint(1,10)
print(num)
print(num2)
