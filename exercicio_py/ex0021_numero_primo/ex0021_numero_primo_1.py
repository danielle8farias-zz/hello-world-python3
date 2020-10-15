#!/usr/bin/env python3.8

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita um número natural inteiro e programa verifica se esse é número primo.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_nat

def verificar_primo(n):
    raiz = int(n ** (0.5))
    #raiz+1 para incluir a própria raiz; pois range tem intervalo aberto
    for divisor in range(2, raiz+1):
        if n % divisor == 0:
            return False
    return True

ler_cabecalho('verifica se é primo')
while True:
    num = ler_num_nat("Digite um número inteiro: ")
    resultado = verificar_primo(num)
    if resultado:
        print('É PRIMO!\n')
    else:
        print("não é primo\n")
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()

####    explicação do uso da raiz   ####
# n = 2 * a
#    a = n / 2
#    pois não existe divisor que seja maior do que a metade do número ou menor do que ele mesmo
# n = a * b
#    b = n / a
# se a > raiz(n), então n/a < n/raiz(n)
#    efetuando os cálculos de radiciação para retitrar a raiz do denominador, temos
#    n/a < raiz(n), logo b < raiz(n)
