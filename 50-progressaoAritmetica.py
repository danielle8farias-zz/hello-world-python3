'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('DEZ PRIMEIROS TERMOS DE UMA PA')

while True:
    A1 =  int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    An = A1 + (10-1)*r
    for n in range(A1, An + r, r):
        print('{}'.format(n), end = '- ')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
