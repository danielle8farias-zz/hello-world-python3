from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 15)
print('Computador jogou {}.'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você VENCEU!')
    elif jogador == 2:
        print('O computador venceu.')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('O computador venceu.')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você VENCEU!')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('Você VENCEU!')
    elif jogador == 1:
        print('O computador venceu.')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida')
print('-=' * 15)
