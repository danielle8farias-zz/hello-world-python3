'''
Faça um fatorial que tenha a opção de mostrar os números decrescente da fatoração.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('fatorial')

def fat(n, show = False):
    f = 1
    while n > 0:
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(f' = {f}', end='')
        f *= n
        n -= 1
    return f


while True:
    n = int(input('Número: '))
    fatorial = fat(n, show=True)
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
