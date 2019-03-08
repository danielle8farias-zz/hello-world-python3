'''
Leia um número e retorne seu fatorial.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('FATORIAL!')

def fat(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


while True:
    n = int(input("Digite um número: "))
    print(f'O fatorial é {fat(n)}.')
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
