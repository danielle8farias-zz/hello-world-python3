########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Dado uma matriz, o programa retorna a sua transposta.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, criar_linha
from funcoes_matriz import ler_matriz, imprimir_matriz

def matriz_nula(Ai, Aj):
    N = []
    for i in range(Ai):
        # criando as colunas dentro de cada linha
        linha = [0] * Aj
        N.append(linha)
    return N


def matriz_transposta(M):
    n_linhas = len(M)
    n_colunas = len(M[0])
    T = matriz_nula (n_colunas, n_linhas)
    for i in range(n_linhas):
        for j in range(n_colunas):
            # invertendo as posições pois é propriedade da matriz transposta
            T[j][i]= M[i][j]
    return T


ler_cabecalho('matriz transposta:')
arquivo = 'matriz_exemplo.txt'
matriz = ler_matriz(arquivo)
n_linhas = len (matriz)
n_colunas = len(matriz[0])
print()
imprimir_matriz(matriz, n_linhas, n_colunas)
criar_linha()
matriz_T = matriz_transposta(matriz)
imprimir_matriz(matriz_T, n_colunas, n_linhas)
print()
criar_rodape()
