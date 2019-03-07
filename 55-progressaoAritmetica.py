'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('DEZ PRIMEIROS TERMOS DE UMA PA')

while True:
    A1 =  int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    cont = 1
    An = A1
    while cont <= 10:
        print('{}'.format(An), end=' ')
        print(' - ' if cont < 10 else ' ', end=' ')
        An = An + r
        cont += 1
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
