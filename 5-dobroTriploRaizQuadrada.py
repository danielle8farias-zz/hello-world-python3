'''
Digite um número e mostro o dobro, o triplo e a raiz quadrada.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('DOBRO, TRIPLO E RAÍZ QUADRADA')

while True:
    num = float(input('Digite um número: '))
    dobro = num*2
    print('O dobro de {} é {}'.format(num, dobro))
    triplo = num*3
    print('O triplo de {} é {}'.format(num, triplo))
    raiz = num**(1/2)
    print('A raiz quadrada de {} é {}'.format(num, raiz))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break

rodape()
