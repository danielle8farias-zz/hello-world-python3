'''
Usuário digita valores numa matriz 3 x 3. Programa retorna essa matriz.
'''

linha = list()
coluna = list()

#criando as colunas da matriz
for l in range(3):
    #criando as linhas da matriz
    for c in range(3):
        elem = int(input(f'Digite o elemento A{l}{c}: '))
        linha.append(elem)  
    #adicionando a linha na matriz
    coluna.append(linha[:])
    #limpando a linha anterior para que não haja repetições
    linha.clear()

print()
for i in range(3):
    print(coluna[i])

print('\n')

#outra solução
#inicializando a matriz com a posições
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o A{l}{c} elemento: '))

print()
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
