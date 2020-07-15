#!/usr/bin/env python3.8

'''
Usuário digita um número natural inteiro e programa verifica se esse é número primo. Com validação de dados.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_nat


def verificar_primo(n):
    #verificando se o número dado é divisível de 2 até n-1
    #   (lembrar que o range é de intervalo aberto no final)
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


ler_cabecalho('verifica se é primo')
while True:
    num = ler_num_nat("Digite um número inteiro: ")
    resultado = verificar_primo(num)
    if resultado:
        print('É PRIMO!')
    else:
        print("não é primo")
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
rodape()
