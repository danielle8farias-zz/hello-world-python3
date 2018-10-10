'''
Dados os catetos, calcule o valor da hipotenusa.
'''
print('-'*50)
print('{: ^50}'.format('CÁLCULO DA HIPOTENUSA'))
print('-'*50)
from math import sqrt
b = float(input('Digite o primeiro cateto: '))
c = float(input('Digite o segundo cateto: '))
a = sqrt(b**2 + c**2)
print('O valor da hipotenusa é: {}'.format(a))

'''
from math import hypot
a = hypot(b, c)
'''
