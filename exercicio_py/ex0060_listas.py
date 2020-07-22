'''
Propriedades de uma lista.
'''

frutas = ['maçã', 'laranja', 'banana', 'uva']
print(frutas)

#adicionando item ao final da lista
frutas.append('morango')
print(frutas)
frutas.append('melão')
print(frutas)

#adicionando item em uma determinada posição
frutas.insert(0, 'kiwi')
print(frutas)
#insert(posição, item)
frutas.insert(2, 'melancia')
print(frutas)

#excluindo itens da lista
del frutas[5]
print(frutas)
#sem parâmetro, remove o último item da lista
frutas.pop()
print(frutas)
frutas.pop(1)
print(frutas)
#revomendo pelo nome do item
frutas.remove('melancia')
print(frutas)

#verificando se o item existe na lista antes de tentar removê-lo
if 'laranja' in frutas:
    #se houver mais de 1 item, remove a 1ª ocorrência
    frutas.remove('laranja')
print(frutas)

if 'pessego' not in frutas:
    frutas.append('pessego')
print(frutas)

#mostra o índice e o item
for i in enumerate(frutas):
    print(i)
print()

#ordenando a lista
frutas.sort()
print(frutas)
#ordem decrescente
frutas.sort(reverse=True)
print(frutas)

#criando uma lista de números com range()
valores = list(range(3,9))
print(valores)


#mudando um item da lista
print(valores)
valores[2] = 7
print(valores)

numeros = list()
numeros.append(8)
numeros.append(9)
numeros.append(0)

for n in numeros:
    print(f'{n}...', end='')
print('\n')

for i, n in enumerate(numeros):
    print(f'número {n} na {i}ª posição')

for i in enumerate(numeros):
    print(i)
print()

#clonando listas
comida = frutas
print(comida)
frutas.append('limão')
print(comida)

#copiando listas
comida = frutas[:]
print(frutas)
comida.pop()
print(comida)
print(frutas)

#desempacotando lista
lista1 = [1, 2, 3, 4, 5]
n1, n2, *n = lista1
print(n1, n2, n)
