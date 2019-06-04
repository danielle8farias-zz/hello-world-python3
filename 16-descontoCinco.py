'''
Leia o valor e desconte 5%.
'''
from mensagem import cabecalho
from mensagem import rodape

#função
def desconto(preco):
    desconto = preco - (preco*0.05)
    return desconto

#programa principal
cabecalho('DESCONTO 5%')
while True:
    preco = float(input('Digite o preço: R$'))
    valor_desconto = desconto(preco)
    print(f'O novo preço com desconto de 5% é R${valor_desconto:.2f}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
