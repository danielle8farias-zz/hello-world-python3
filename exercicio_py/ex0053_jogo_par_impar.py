'''
Usuário escolhe um número inteiro entre 0 e 10. Programa também escolherá um 
número nesse intervalo. Usuário informa se acha que a soma desses dois valores 
será par ou ímpar. O programa é interrompido quando o usuário perder, mostrando 
ao final o total de vitórias.
'''

from random import randint

print('Jogo de par ou ímpar')
print()
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
    print()
    print(f'O computador escolheu: {computador}')
    print(f'Soma: {total}')
    if resposta == escolha:
        print('Você venceu!')
        i += 1
    else:
        print('você perdeu...')
        print()
        break
    print()
print(f'Total de vitórias: {i}')
print()
