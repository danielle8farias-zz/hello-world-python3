'''
Faça um jogo de adivinhação de números, entre os números 0 a 5.
Usuário digita um número, computador escolhe um número e se os números forem
os mesmos, usuário ganha.
'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 13)
print('Por favor escolha um número de 0 a 5')
print('-=-' * 13)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu adivinhar!')
else:
    print('Eu pensei no número {}.'.format(computador))
