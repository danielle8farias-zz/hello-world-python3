'''
Calcule o preço de um aluguel de um carro, sabendo que custa R$60,00
por dia e R$0,15 por quilômetro rodado.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('PREÇO ALUGUEL DE CARRO')
while True:
    dias = int(input('Dias alugados: '))
    km = float(input('Quilometros rodados: '))
    preco = dias*60 + km*0.15
    print('O total a pagar foi R${:.2f}'.format(preco))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
