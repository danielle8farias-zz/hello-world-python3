########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Dado uma matriz, o programa retorna a sua transposta.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, criar_linha
from funcoes_matriz import ler_matriz, imprimir_matriz, matriz_transposta


ler_cabecalho('matriz:')
arquivo = 'matriz_exemplo.txt'
matriz = ler_matriz(arquivo)
n_linhas = len (matriz)
n_colunas = len(matriz[0])
imprimir_matriz(matriz, n_linhas, n_colunas)
matriz_T = matriz_transposta(matriz)
ler_cabecalho('matriz transposta:')
imprimir_matriz(matriz_T, n_colunas, n_linhas)
print()
criar_rodape()
