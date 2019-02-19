'''
Informe a raiz quadrada de um número inteiro.
'''
from mensagem import cabecalho
from mensagem import rodape
from math import sqrt

cabecalho('RAÍZ QUADRADA')

while True:
    num = int(input('digite um número inteiro: '))
    raiz = sqrt(num)
    print()
    print('A raiz de {} = {}'.format(num, raiz))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break

rodape()
