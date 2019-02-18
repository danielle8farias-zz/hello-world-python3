'''
Faça um conversos de Real em Dolar.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('CONVERSOR REAL EM DOLAR')

while True:
    real = float(input('Valor em Reais: R$'))
    dolar = real/3.86
    print()
    print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
