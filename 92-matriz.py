'''
Crie um programa para criar uma matriz.
'''
print('-'*50)
print('{:^50}'.format('MATRIZES'))
print('-'*50)
num_linha = int(input('Digite o número de linhas: '))
num_coluna = int(input('Digite o número de colunas: '))
matriz = []
for i in range(num_linha):
    linhas = []
    for j in range(num_coluna):
        valor = input(f'Digite o valor de A{i}{j}: ')
        linhas.append(valor)
    matriz.append(linhas)
#imprimindo formatado
print()
for i in range(num_linha):
    for j in range(num_coluna):
        print(f'[{matriz[i][j]:^4}]', end='')
    print()
print('-'*50)
print('{:^50}'.format('FIM'))
print('-'*50)
