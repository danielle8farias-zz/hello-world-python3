'''
Dê ao usuario um número aleatório entre 0 e 1.
E outro número aleatório entre 1 e 10.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
import random

#função que retorna um número aleatório entre 0 e 1
def num_aleatorio1():
    num = random.random()
    return num

#função que retorna um número aleatório entre 1 e 10
def num_aleatorio2():
    num = random.randint(1,10)
    return num

#programa principal
cabecalho('NÚMEROS ALEATÓRIOS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num1 = num_aleatorio1()
    num2 = num_aleatorio2()
    print(f'Primeiro número aleatório entre 0 e 1: {num1}')
    print(f'Segundo número aleatório entre 1 e 10: {num2}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
