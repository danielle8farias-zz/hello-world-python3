'''
Usando deepcopy com lista dentro de um dicionário
'''

dicio1 = {1:'a', 2:'b', 3:'c', 'd':[7,8,9]}
print('dicionário 1')
print(dicio1)
print()

dicio2 = dicio1
print('dicionário 2')
print(dicio2)
print()

#mudando item de índice 1
print('mudando item de índice 1 do dicionário 2')
dicio2[1] = 'AA'
print('dicionário2')
print(dicio2)
print('dicionário 1')
print(dicio1)
print('dicionário 1 é igual ao dicionário 2?')
print(dicio1 == dicio2)
print()

dicio3 = dicio1.copy()
print('Copiando dicionário 1 para dicionário 3')
print(dicio3)
print('alterando valor do item 2 no dicionário 3')
dicio3[2] = 'BB'
print('dicionário 1')
print(dicio1)
print('dicionário 3')
print(dicio3)
print('dicionário 1 é igual ao dicionário 3?')
print(dicio3 == dicio1)
print()

print('alterando o valor do item "d"[0] do dicionário 3')
dicio3['d'][0] = 24
print('dicionário 3')
print(dicio3)
print('dicionário 1')
#valor da lista foi alterado nos 2 dicionários
print(dicio1)
print()

import copy
dicio4 = copy.deepcopy(dicio1)
print('dicionário 1')
print(dicio1)
print('copiando o dicionário 1 para o dicionário 4')
print(dicio4)
dicio4['d'][0] = 88
print('Alterando o item "d"[0] do dicionário 4 depois do deepcopy')
print(dicio4)
print('dicionário 1')
print(dicio1)
print()
