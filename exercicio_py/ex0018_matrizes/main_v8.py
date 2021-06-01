########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Dado duas matrizes, verificar sua igualdade.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, criar_linha
from funcoes_matriz import ler_matriz, imprimir_matriz, igualdade


ler_cabecalho('Igualdade de matrizes:')

arquivo1 = 'matriz_exemplo.txt'
matriz_A = ler_matriz(arquivo1)
n_linhasA = len (matriz_A)
n_colunasA = len(matriz_A[0])
print('\nMatriz A:')
imprimir_matriz(matriz_A, n_linhasA, n_colunasA)
criar_linha()

arquivo2 = 'matriz4x5.txt'
matriz_B = ler_matriz(arquivo2)
n_linhasB = len (matriz_B)
n_colunasB = len(matriz_B[0])
print('Matriz B:')
imprimir_matriz(matriz_B, n_linhasB, n_colunasB)
criar_linha()

print('Comparando A com B:')
if igualdade(matriz_A, matriz_B):
    print('As matrizes são iguais!')
else:
    print('As matrizes NÃO são iguais.')
print()

print('Comparando A com A:')
if igualdade(matriz_A, matriz_A):
    print('As matrizes são iguais!')
else:
    print('As matrizes NÃO são iguais.')
print()

print('Comparando B com B:')
if igualdade(matriz_B, matriz_B):
    print('As matrizes são iguais!')
else:
    print('As matrizes NÃO são iguais.')
print()


criar_rodape()
