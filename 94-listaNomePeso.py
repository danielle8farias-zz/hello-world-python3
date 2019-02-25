'''
Faça um programa que leia o nome e o peso de várias pessoas, guardando esses valores numa lista.
Retorne quantas pessoas foram cadastradas, a lista das pessoas mais pesadas e a lista das pessoas
mais leves.
'''

lista = []
maior = menor = 0
while True:
    nome_peso = []
    nome = input('Digite o nome: ')
    nome_peso.append(nome)
    peso = float(input('Digite o peso: '))
    nome_peso.append(peso)
    
    if len(lista) == 0:
        maior = menor = nome_peso[1]
    else:
        if nome_peso[1] > maior:
            maior = nome_peso[1]
        if nome_peso[1] < menor:
            menor = nome_peso[1]

    lista.append(nome_peso)
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print(f'Número de pessoas cadastradas: {len(lista)}')
print(f'O maior peso foi {maior} Kg. De ', end='')
for i in lista:
    if i[1] == maior:
        print(f'{i[0]}',end=', ')
print()
print(f'O menor peso foi {menor} Kg. De ', end='')
for i in lista:
    if i[1] == menor:
        print(f'{i[0]}',end=', ')
print()
