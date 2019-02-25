'''
Faça uma matriz 3 x 3 que leia os valores pelo teclado e retorne a soma de todos os valores pares,
a soma dos valores da terceira coluna e o maior valor da segunda linha.
'''
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor de A{i}{j}: '))
        linha.append(valor)
    matriz.append(linha)
print()
#imprimindo a matriz
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^4}]',end='')
    print()
#verificando valores pares
soma_pares = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
print(f'A soma dos valores pares é: {soma_pares}')
#soma dos valores da terceira coluna
soma_coluna = 0
for i in range(3):
    soma_coluna += matriz[i][2]
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
#maior valor da segunda linha
maior = 0
for i in range(3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]
print(f'O maior valor da segunda linha é: {maior}')
