'''
Faça um programa que some duas matrizes.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('SOMA DE DUAS MATRIZES')

def matriz (num_linhas, num_colunas):
    coluna = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input(f'Digite o valor A{i}{j}: '))
            linha.append(valor)
        coluna.append(linha)
    return coluna


def linha_coluna ():
    num_linhas = int(input('Digite o número de linhas: '))
    num_colunas = int(input('Digite o número de colunas: '))
    return matriz (num_linhas, num_colunas)


def soma_matriz (A, B):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    soma = []
    for i in range(num_linhas):
        for j in range(num_colunas):
            soma.append(A[i][j] + B[i][j])
    return soma


A = linha_coluna()

B = linha_coluna()
print(f'Matriz B = {B}')
print()
soma = soma_matriz(A, B)
print(f'A soma das matrizes é = {soma}')

rodape()
