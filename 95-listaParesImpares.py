'''
Crie um programa onde o usuário deve digitar 7 valores e coloque-os em uma única lista. Dentro dessa
lista os valores devem ser separados em duas listas, contendo os números pares e ímpares.
Ao final mostre os valores em ordem crescente.
'''
lista = [[],[]]
n = 1
while n <= 7 :
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0 :
        lista[0].append(valor)
    else:
        lista[1].append(valor)
    n += 1
    lista[0].sort()
    lista[1].sort()

print(lista)