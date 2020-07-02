#!/usr/bin/env python3.8

'''
Usuário fornece um número inteiro que será o tamanho do array, 
em seguida insere números que serão elementos desse array.
O programa retorna a soma desses elementos.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
from numeros import ler_num_int, ler_num_float


def somar_vetor(num):
    lista = []
    i = 1
    soma = 0
    for i in range(i, num+1):
        elemento = ler_num_float(f'Digite o {i}º número: ')
        soma += elemento
        lista.append(elemento)
    return lista, soma


#programa principal
ler_cabecalho('soma array')
while True:
    print('Escolhendo o tamanho do vetor...')
    tamanho_vetor = ler_num_int('Digite um número inteiro: ')
    #as variáveis 'lista' e 'soma' recebem os retornos da função
    lista, soma = somar_vetor(tamanho_vetor)
    print()
    print(f'Vetor: {lista}')
    print(f'Soma dos elementos do vetor: {soma}')
    print()
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    if resposta == 'N':
        break
    else:
        linha()
        print()
rodape()
