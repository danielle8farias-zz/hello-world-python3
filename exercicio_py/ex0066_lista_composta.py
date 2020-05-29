'''
Utilizando lsitas compostas.
'''

lista1 = list()
lista1.append('Gustavo')
lista1.append(40)
print(lista1)

lista2 = list()
#adicionando uma lista dentro de outra lista
lista2.append(lista1[:])
print(lista2)

#criando novos elementos para lista
lista1[0] = 'Maria'
lista1[1] = 30
lista2.append(lista1[:])
print(lista2)

lista3 = [['João', 19], ['Ana', 34], ['Davi', 13], ['Madalena', 50]]
print(lista3)
print(lista3[0])
print(lista3[0][0])

for p in lista3:
    print(p)

for p in lista3:
    print(p[0])

for p in lista3:
    print(p[1])

for p in lista3:
    print(f'{p[0]} tem {p[1]} anos.\n')


pessoas = list()
dados = list()

for i in range(3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    #limpando a lista
    dados.clear()

print(pessoas)
