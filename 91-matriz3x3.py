'''
Crie uma matriz 3x3 que leia os valores pelo teclado. Ao final imprima a formatação correta.
'''
print('-'*50)
print('{:^50}'.format('MATRIZ 3 X 3'))
print('-'*50)
matriz = []
for i in range(3):
    linhas = []
    for j in range(3):
        valor = int(input(f'Digite o valor de A{i}{j}: '))
        linhas.append(valor)
    matriz.append(linhas)
print()
#imprimindo
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end='')
    print()
print()
print('-'*50)
print('{:^50}'.format('FIM'))
