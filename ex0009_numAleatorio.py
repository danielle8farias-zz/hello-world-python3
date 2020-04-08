#!/usr/bin/env python3.8

'''
Dê ao usuario um número aleatório entre 0 e 1.
E outro número aleatório entre 1 e 10.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/exercicios-python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape
from random import randint, random

def num_aleatorio():
    #função que retorna um número aleatório entre 0 e 1
    num1 = random()
    #função que retorna um número aleatório entre 1 e 10
    num2 = randint(1,10)
    # dois retornos
    return num1, num2

#programa principal
cabecalho('NÚMEROS ALEATÓRIOS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    # duas variáveis recebem os retornos da função
    num1, num2 = num_aleatorio()
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
