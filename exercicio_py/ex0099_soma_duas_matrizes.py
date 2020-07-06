'''
Usuário digita duas matrizes, escolhendo a ordem dessas e programa retorna a soma entre elas.
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


def somar_matrizes (A, B):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    soma = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor_soma = (A[i][j] + B[i][j])
            linha.append(valor_soma)
        soma.append(linha)
    return soma

while True:
    ler_cabecalho('soma duas matrizes')
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    if Ai == Bi and Aj == Bj:
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
        resultado = somar_matrizes(A, B)
        #imprimindo a soma
        sleep(0.5)
        print('\nResultado da soma:')
        for i in range(Ai):
            for j in range(Aj):
                sleep(0.5)
                print(f'[{resultado[i][j]:^5}]', end='', flush=True)
            print()
        print()
    else:
        print('Não é possível somar: As matrizes devem ser de mesma ordem.')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
sleep(0.5)
rodape()
