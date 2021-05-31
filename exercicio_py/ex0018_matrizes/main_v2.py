########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário escolhe o tamanho da matriz e digita o valor dos seus elementos. O programa retorna essa matriz formatada na tela.
########

from funcoes_matriz import construir_matriz

num_linha = int(input('Digite o número de linhas: '))
num_coluna = int(input('Digite o número de colunas: '))

matriz = construir_matriz(num_linha, num_coluna)
print()

for i in range(num_linha):
    for j in range(num_coluna):
        print(f'[{matriz[i][j]:^4}]', end='')
    print()
