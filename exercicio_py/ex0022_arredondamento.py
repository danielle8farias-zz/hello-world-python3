'''
Arredondamento de um número real
'''

#importando módulos de arredondamento
from math import ceil, floor, trunc

num = 3.459214

print(f'Arredondamento para cima: {ceil(num)}')
print(f'Arredondamento para baixo: {floor(num)}')
print(f'Descartando os decimais: {trunc(num)}')
print(f'{num:.0f}')
print()
