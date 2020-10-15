########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro entre 0 e 9999 e programa retorna a posição decimal de cada algarismo; unidade, dezena, centena, etc.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_int


def separar_digitos(num):
    #separando a unidade
    u = num % 10
    print(f'Unidade: {u}')
    #//10 retirando a unidade; %10 separando a dezena(unidade que sobrou)
    d = num // 10 % 10
    print(f'Dezena: {d}')
    #//100 retirando a centena; %10 separando a centena(unidade que sobrou)
    c = num // 100 % 10
    print(f'Centena: {c}')
    #//1000 retirando a unidade de milhar; %10 separando a unidade de milhar(unidade que sobrou)
    um = num // 1000
    print(f'Unidade de Milhar: {um}')


#programa principal
ler_cabecalho('posição decimal')
while True:
    while True:
        print('Escolha um número inteiro entre 0 e 9999')
        num = ler_num_int('Digite um número: ')
        if num >= 0 and num < 10000:
            break
        else:
            print('Número inválido!\n')
    separar_digitos(num)
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('\nDeseja continuar? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()
