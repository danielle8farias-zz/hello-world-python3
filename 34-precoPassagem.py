'''
Pergunte a distância de uma viagem em Km e calcule o preço da passagem
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens
mais longas.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('PREÇO DA PASSAGEM')

while True:
    distancia = float(input('Qual a distância da viagem?(Km) '))
    if distancia <= 200:
        preco = distancia * 0.5
    else:
        preco = distancia * 0.45
    print('Preço da passagem R${:.2f}'.format(preco))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
