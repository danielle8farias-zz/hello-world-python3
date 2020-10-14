########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Jogo do par ou ímpar:
#           Usuário escolhe um número inteiro entre 0 e 10.
#           Programa também escolherá um número no mesmo intervalo, porém sem retornar o valor ao usuário.
#           Usuário informa se acha que a soma desses dois valores será par ou ímpar.
#           O jogo termina quando o usuário perde, mostrando o total de vitórias.
########

from random import randint
from time import sleep

print('Jogo de par ou ímpar\n')
i = 0
while True:
    jogador = int(input('Digite um número inteiro [0 a 10]: '))
    computador = randint(0,10)
    total = jogador + computador
    if total % 2 == 0:
        resposta = 'p'
    else:
        resposta = 'i'
    escolha = ' '
    while escolha not in 'pi':
        escolha = input('Par [p] ou Ímpar [i] ? ').lower().strip()[0]
    sleep(0.5)
    print(f'\nO computador escolheu: {computador}')
    sleep(0.5)
    print(f'Soma: {total}')
    if resposta == escolha:
        print('Você venceu!\n')
        i += 1
    else:
        print('você perdeu...\n')
        break
sleep(0.5)
print(f'Total de vitórias: {i}')
