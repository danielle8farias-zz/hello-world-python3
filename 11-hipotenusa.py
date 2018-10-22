'''
Dados os catetos, calcule o valor da hipotenusa.
'''
print('-'*50)
print('{: ^50}'.format('CÁLCULO DA HIPOTENUSA'))
print('-'*50)
from math import sqrt
while True:
    b = float(input('Digite o primeiro cateto: '))
    c = float(input('Digite o segundo cateto: '))
    a = sqrt(b**2 + c**2)
    print()
    print('O valor da hipotenusa é: {}'.format(a))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
'''
from math import hypot
a = hypot(b, c)
'''
