'''
Leia o ano de nascimento de 7 pessoas. Mostre quantas são maiores de 21
e quantas são menores.
'''
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Existem {} pessoas maiores de idade.'.format(maior))
print('Existem {} pessoas menores de idade.'.format(menor))
