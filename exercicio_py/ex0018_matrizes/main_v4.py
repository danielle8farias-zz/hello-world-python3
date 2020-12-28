########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita duas matrizes, escolhendo a ordem dessas e programa retorna a multiplicação entre elas.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, ler_resposta
from numeros import ler_num_int, ler_num_float
from construir_matriz import construir_matriz
from time import sleep


def linha_coluna ():
    num_linhas = ler_num_int('Digite o número de linhas: ')
    num_colunas = ler_num_int('Digite o número de colunas: ')
    return num_linhas, num_colunas


def imprimir_matriz(M, Mi, Mj):
    for i in range(Mi):
        for j in range(Mj):
            sleep(0.5)
            print(f'[{M[i][j]:^5}]', end='', flush=True)
        print()


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
        imprimir_matriz(A, Ai, Aj)
        print()
        sleep(0.5)
        print('Matriz B:')
        imprimir_matriz(B, Bi, Bj)
        print()
        resultado = multiplicar_matrizes(A, B)
        #imprimindo a multiplicação
        sleep(0.5)
        print('\nResultado da multiplicação das matrizes:')
        imprimir_matriz(resultado, Ai, Bj)
        print()
    else:
        print('Não é possível multiplicar: O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
sleep(0.5)
criar_rodape()
