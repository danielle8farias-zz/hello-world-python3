'''
Usuário escolhe o tamanho da matriz e digita o valor dos seus elementos. 
Programa retorna essa matriz.
'''

num_linha = int(input('Digite o número de linhas: '))
num_coluna = int(input('Digite o número de colunas: '))
matriz = list()

for i in range(num_linha):
    #uma nova lista de linha é criada a cada laço
    #   não precisa limpar a lista ao final do laço
    linhas = []
    for j in range(num_coluna):
        valor = input(f'Digite o valor de A{i}{j}: ')
        linhas.append(valor)
    matriz.append(linhas)

print()

for i in range(num_linha):
    for j in range(num_coluna):
        print(f'[{matriz[i][j]:^4}]', end='')
    print()
