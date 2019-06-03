'''
Dados os catetos, calcule o valor da hipotenusa.
'''
from mensagem import cabecalho
from mensagem import rodape
from math import sqrt

#função
def hipotenusa(b,c):
    a = sqrt(b**2 + c**2)
    return a

#programa principal
cabecalho('CÁLCULO DA HIPOTENUSA')
while True:
    b = float(input('Digite o primeiro cateto: '))
    c = float(input('Digite o segundo cateto: '))
    h = hipotenusa(b,c)
    print(f'O valor da hipotenusa é: {h}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()

'''
Também pode ser feito assim:
from math import hypot
a = hypot(b, c)
'''
