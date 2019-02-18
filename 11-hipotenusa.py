'''
Dados os catetos, calcule o valor da hipotenusa.
'''
from mensagem import cabecalho
from mensagem import rodape
from math import sqrt

cabecalho('CÁLCULO DA HIPOTENUSA')

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

rodape()

'''
from math import hypot
a = hypot(b, c)
'''
