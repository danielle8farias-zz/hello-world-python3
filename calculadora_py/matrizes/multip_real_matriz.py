import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float

from matrizes.ordem_matriz import linha_coluna
from matrizes.construcao_matriz import construir_matriz
from matrizes.impressao_matriz import imprimir_matriz

from time import sleep


#efetuando multiplicação por número real
def efetuar_multi_real(A, n):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    multi_real = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = (n * A[i][j])
            linha.append(valor)
        multi_real.append(linha)
    return multi_real


#chamada principal da multiplicação de uma matriz por um número real
def multiplicacao_real():
    ler_cabecalho('multiplicação por um número real')
    #definindo a ordem das matrizes 
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    num = ler_num_float('Digite um número que deseja multiplicar: ')
    print()
    #construindo a matriz
    print('Construindo matriz A')
    A = construir_matriz(Ai, Aj)
    print()
    #imprimindo a matriz
    sleep(0.5)
    print('Matriz A:')
    imprimir_matriz(A, Ai, Aj)
    sleep(0.5)
    resultado = efetuar_multi_real(A, num)
    #imprimindo a multiplicação por real
    sleep(0.5)
    print('\nResultado da multiplicação por número real:')
    imprimir_matriz(resultado, Ai, Aj)
    print()
