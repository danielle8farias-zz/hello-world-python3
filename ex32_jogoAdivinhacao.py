'''
Faça um jogo de adivinhação de números, entre os números 0 a 5.
Usuário digita um número, computador escolhe um número e se os números forem
os mesmos, usuário ganha.
'''
#importando parte do código
from random import randint
from time import sleep
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha

#programa principal
cabecalho('jogo adivinhação')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    computador = randint(0, 5)
    linha()
    print('Por favor escolha um número de 0 a 5')
    linha()
    jogador = int(input('Em que número eu pensei? '))
    print('Processando...')
    sleep(2)
    if jogador == computador:
        print('PARABÉNS! Você conseguiu adivinhar!')
    else:
        print(f'Eu pensei no número {computador}.')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
