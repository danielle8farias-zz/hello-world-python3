'''
Crie um caixa eletrônico. Pergunte ao usuário qual valor a ser sacado (número
inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues. O caixa possui cédulas de 50, 20, 10 e 1.
'''
print('-'*50)
print('{: ^50}'.format('CAIXA ELETRÔNICO'))
print('-'*50)
valor = int(input('Valor a ser sacado: R$'))
if valor >= 50:
    notas = valor//50
    valor = valor % 50
    print('{} notas de R$50'.format(notas))
if valor >= 20:
    notas = valor//20
    valor = valor % 20
    print('{} notas de R$20'.format(notas))
if valor >= 10:
    notas = valor//10
    valor = valor % 10
    print('{} notas de R$10'.format(notas))
if valor >= 1:
    notas = valor//1
    valor = valor % 1
    print('{} notas de R$1'.format(notas))
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
