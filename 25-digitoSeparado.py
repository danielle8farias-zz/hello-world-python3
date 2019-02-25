'''
Leia um número de 0 a 9999 e mostre cada um dos dígitos.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('DÍGITOS DE UM NÚMERO')

while True:
    num = int(input('Digite um número: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    um = num // 1000 % 10
    dm = num // 10000 % 10
    cm = num // 100000 % 10
    print('Unidade: {}'.format(u))
    print('Dezena: {}'.format(d))
    print('Centena: {}'.format(c))
    print('Unidade de Milhar: {}'.format(um))
    print(f'Dezena de Milhar: {dm}')
    print(f'Centena de Milhar: {cm}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
