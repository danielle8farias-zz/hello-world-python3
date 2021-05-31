########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Multiplicação de uma matriz por um número.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, criar_linha
from numeros import ler_num_nat, ler_num_float
from funcoes_matriz import construir_matriz, imprimir_matriz, multiplicar_real


ler_cabecalho('matriz x número')
linha = ler_num_nat('Digite o número de linhas: ')
coluna = ler_num_nat('Digite o número de colunas: ')
print()
matriz_A = construir_matriz(linha, coluna)
print()
imprimir_matriz(matriz_A, linha, coluna)
num = ler_num_float('\nDigite um número para multiplicar: ')
matriz_M = multiplicar_real(matriz_A, num)
criar_linha()
print('Nova matriz multiplicada:')
criar_linha()
imprimir_matriz(matriz_M, linha, coluna)
print()
criar_rodape()
