'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
Pergunta se o usuário quer mostrar mais termos.
Quando escolhido 0 termos o programa encerra.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('TERMOS DE UMA PA')

while True:
    A1 =  int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    cont = 1
    An = A1
    total = 0
    mais = 10
    while mais != 0:
        total += mais
        while cont <= total:
            print('{} - '.format(An), end='')
            An = An + r
            cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
    print('Foram mostrados {} termos.'.format(total))
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
