########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita valores numa matriz 3 x 3. Programa retorna essa matriz formatada na tela.
########

#inicializando a matriz com a posições
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o A{l}{c} elemento: '))

print()
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
