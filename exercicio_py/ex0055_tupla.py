'''
Cardápio de refeições organizado por tuplas.
'''

#criando tuplas
cafe_manha = ('mamão', 'leite', 'ovos', 'pão', 'café', 'aveia', 'queijo', 'iogurte')
almoco = ('carne soja', 'arroz', 'cenoura', 'feijão', 'abóbora', 'tomate', 'couve', 'brócolis')
jantar = ('leite', 'chá', 'sopa', 'pão', 'mingau', 'uva', 'aveia', 'maçã')

print('Cardápio das refeições:')
print(f'Café da manhã: {cafe_manha}')
print(f'Almoço: {almoco}')
print(f'Jantar: {jantar}')

print(f'''
Pedido 1:
café da manhã: {cafe_manha[-1]}, {cafe_manha[4]}, {cafe_manha[2]}
almoço: {almoco[1]}, {almoco[3]}, {almoco[-1]}
jantar: {jantar[2]}, {jantar[3]}, {jantar[-3]}
''')
print(f'''
Pedido 2:
café da manhã: {cafe_manha[2:5]}
almoço: {almoco[5:]}
jantar: {jantar[:3]}
''')

print('No café da manhã, eu posso comer: ', end='')
for comida in cafe_manha:
    print(comida, end=', ')
print('\n')

print('No almoço, eu posso comer: ')
for i in range(0, len(almoco)):
    print(f'{almoco[i]} - na posição {i}')
print()

print('No jantar, eu posso comer: ')
for i, comida in enumerate(jantar):
    print(f'{comida}, no item: {i}')
print()

cardapio = cafe_manha + almoco + jantar
print(cardapio)
print(type(cardapio))
cardapio = jantar + cafe_manha + almoco
print(cardapio)
#quantas vezes aparece o item
print(cardapio.count('leite'))
#posição de um item
print(cardapio.index('queijo'))
#encontre  quantos itens há a partir da posição
#   index(item, posição)
print(cardapio.index('leite', 1))
#apagando da memória
del(cardapio)
