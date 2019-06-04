'''
Faça um conversos de Real em Dolar.
'''
from mensagem import cabecalho
from mensagem import rodape

#função
def dollar(real):
    dolar = real/3.89 #em 03/06/2019
    return dolar

#programa principal
cabecalho('CONVERSOR REAL EM DOLAR')
while True:
    real = float(input('Valor em Reais: R$'))
    valor_dolar = dollar(real)
    print(f'Com R${real:.2f} você pode comprar US${valor_dolar:.2f}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
