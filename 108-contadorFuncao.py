'''
Faça um função contadora que receba o termo inicial, final e o passo.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('contador')

def contagem(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print()
    elif i > f:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print()

while True:
    i = int(input('Início: '))
    f = int(input('Final: '))
    p = int(input('Passo: '))
    contagem(i,f,p)
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
