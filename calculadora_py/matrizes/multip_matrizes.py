import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho

from matrizes.ordem_matriz import linha_coluna
from matrizes.construcao_matriz import construir_matriz
from matrizes.impressao_matriz import imprimir_matriz

from time import sleep


#efetuar multiplicação de matrizes
def efetuar_multi_matriz(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_colunas_B, num_colunas_B = len(B), len(B[0])
    multiplicacao = list()
    for i in range(num_linhas_A):
        linha = []
        for j in range(num_colunas_B):
            soma = 0
            for k in range(num_colunas_A):
                soma += A[i][k] * B[k][j]
            linha.append(soma)
        multiplicacao.append(linha)
    return multiplicacao


#chamada principal da multiplicação de matrizes
def multiplicacao_matriz():
    ler_cabecalho('multiplicação de matrizes')
    #definindo ordem das matrizes
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    if Aj == Bi:
        #construindo as matrizes
        print('Construindo a matriz A')
        A = construir_matriz(Ai, Aj)
        print()
        print('Construindo a matriz B')
        B = construir_matriz(Bi, Bj)
        print()
        #imprimindo as matrizes
        sleep(0.5)
        print('Matriz A')
        imprimir_matriz(A, Ai, Aj)
        print()
        sleep(0.5)
        print('Matriz B')
        imprimir_matriz(B, Bi, Bj)
        resultado = efetuar_multi_matriz(A, B)
        #imprimindo a multiplicação
        sleep(0.5)
        print('\nResultado da multiplicação de matrizes:')
        imprimir_matriz(resultado, Ai, Bj)
    else:
        print('Não é possível multiplicar as matrizes. O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.')
        sleep(0.5)
    print()
