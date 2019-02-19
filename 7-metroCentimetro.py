'''
Transforma metros em centímetros e milímetros.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('CONVERSOR DE METROS PARA CM E MM')

while True:
    metros = float(input('Dê um valor em metros: '))
    cent = metros*100
    mil = metros*1000
    print()
    print('{}m corresponde a {}cm'.format(metros, cent))
    print('{}m corresponde a {}mm'.format(metros, mil))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break

rodape()
