########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa vários números inteiros que serão guardados em uma lista. O programa retorna os valores pares em uma lista separada e ímpares em outra lista. Ao final, as três listas são exibidas.
########

num_lista = list()
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    num_lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
    print()
print()
print(num_lista)
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
