'''
Jogo de adivinhação de números. 
Computador escolhe um número aleatório entre 0 e 10. 
O usuário deve tentar adivinhar esse número escolhido pelo computador para ganhar. 
Caso o usuário na acerte na tentativa, o programa deve retornar uma dica: 
se o número informado pelo usuário é menor ou maior do que aquele que foi escolhido pelo computador. 
No final, deve-se mostrar quantos palpites foram dados até o usuário acertar.
'''

from random import randint
from time import sleep

print('O computador escolheu um número entre 0 e 10.')
print('Você consegue adivinhar qual foi?')
print()

acertou = False
palpite = 0
computador = randint(0, 10)

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    print('Processando...')
    sleep(1)
    palpite += 1
    if jogador == computador:
        print('PARABÉNS! Você conseguiu adivinhar!')
        print(f'Número de tentativas: {palpite}')
        acertou = True
    else:
        if jogador > computador:
            print('Meu número é menor... Tente novamente!')
        else:
            print('Meu número é maior... Tente novamente!')
print()
