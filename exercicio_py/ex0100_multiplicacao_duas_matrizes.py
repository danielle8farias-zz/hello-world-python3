#!/usr/bin/env python3.8

'''
Usuário digita duas matrizes, escolhendo a ordem dessas e programa retorna a multiplicação entre elas.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_int, ler_num_float
from time import sleep


def linha_coluna ():
    num_linhas = ler_num_int('Digite o número de linhas: ')
    num_colunas = ler_num_int('Digite o número de colunas: ')
    return num_linhas, num_colunas


def construir_matriz (num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = ler_num_float(f'Digite o valor A{i}{j}: ')
            linha.append(valor)
        matriz.append(linha)
    return matriz


def multiplicar_matrizes (A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    multiplicacao = []
    for i in range(num_linhas_A):
        linha = []
        for j in range(num_colunas_B):
            soma = 0
            for k in range(num_colunas_A):
                soma += A[i][k] * B[k][j]
            linha.append(soma)
        multiplicacao.append(linha)
    return multiplicacao


while True:
    ler_cabecalho('Multiplicação duas matrizes')
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    if Aj == Bi:
        print('Construindo matriz A')
        A = construir_matriz(Ai, Aj)
        print('\nConstruindo matriz B')
        B = construir_matriz(Bi, Bj)
        print()
        #imprimindo as matrizes
        sleep(0.5)
        print('Matriz A:')
        for i in range(Ai):
            for j in range(Aj):
                sleep(0.5)
                print(f'[{A[i][j]:^5}]', end='', flush=True)
            print()
        print()
        sleep(0.5)
        print('Matriz B:')
        for i in range(Bi):
            for j in range(Bj):
                sleep(0.5)
                print(f'[{B[i][j]:^5}]', end='', flush=True)
            print()
        print()
        resultado = multiplicar_matrizes(A, B)
        #imprimindo a multiplicação
        sleep(0.5)
        print('\nResultado da soma:')
        for i in range(Ai):
            for j in range(Bj):
                sleep(0.5)
                print(f'[{resultado[i][j]:^5}]', end='', flush=True)
            print()
        print()
    else:
        print('Não é possível multiplicar: O número de colunas da 1ª matriz deve ser igual ao número de linhas da 2ª')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
sleep(0.5)
rodape()
