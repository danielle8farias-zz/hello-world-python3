########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita um número natural inteiro e programa verifica se esse é número primo.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_nat

ler_cabecalho('verifica se é primo')
while True:
    n = ler_num_nat("Digite um número inteiro: ")
    i = 0
    c = 0
    while i < n:
        i+= 1
        if (n % i == 0):
            #esse contador serve para guardar quantos divisores o 'num' possui
            c += 1
    #verificando se o c é igual a 2
    #   isso indica que o número dado possui exatamente dois divisores; o que o classifica como primo            
    if c == 2:
        print(f'{"é primo!".upper()}\n')
    else:
        print("não é primo\n")
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
criar_rodape()
