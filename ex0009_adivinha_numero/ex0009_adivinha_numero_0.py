########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Jogo de adivinhação de números:
#           Computador escolhe um número aleatório entre 0 e 10. 
#           O usuário deve tentar adivinhar esse número escolhido pelo computador para ganhar. 
#           Caso o usuário não acerte na tentativa, o programa deve retornar uma dica: se o número informado pelo usuário é menor ou maior do que aquele que foi escolhido pelo computador. 
#           No final, deve-se mostrar quantos palpites foram dados até o usuário acertar.
########

from random import randint
from time import sleep

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape
from numeros import ler_num_int

ler_cabecalho('jogo de adivinhação')
print('O computador escolheu um número entre 0 e 10.')
print('Você consegue adivinhar qual foi?\n')

acertou = False
palpite = 0
computador = randint(0, 10)

while not acertou:
    jogador = ler_num_int('Qual o seu palpite? ')
    print('Processando...')
    sleep(1)
    palpite += 1
    if jogador == computador:
        sleep(0.5)
        print('PARABÉNS! Você conseguiu adivinhar!')
        print(f'Número de tentativas: {palpite}')
        acertou = True
    else:
        sleep(0.5)
        if jogador > computador:
            print('Meu número é menor... Tente novamente!\n')
        else:
            print('Meu número é maior... Tente novamente!\n')
sleep(1)
criar_rodape()
