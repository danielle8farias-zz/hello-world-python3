'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e a condição de pagamento.
à vista dinheiro ofereça desconto de 10%
à vista no cartão ou cheque ofereça desconto de 5%
2x no cartão, preço normal
3x ou mais, 20% de juros
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('LOJAS GUANABARA')

while True:
    preco =  float(input('Preço das compras: R$'))
    print('''FORMAS DE PAGAMENTO
    [1] à vista dinheiro.
    [2] à vista cartão/cheque
    [3] 2x no cartão de crédito
    [4] 3x ou mais no cartão''')
    opcao = int(input('Qual é a opção? '))
    if opcao == 1:
        total = preco - (preco * 0.1)
        print('Sua compra vai custar R${:.2f}'.format(total))
    elif opcao == 2:
        total = preco - (preco * 0.05)
        print('Sua compra vai custar R${:.2f}'.format(total))
    elif opcao == 3:
        total = preco/2
        print('Sua compra será parcelada em 2x de R${:.2f}'.format(total))
    elif opcao == 4:
        total = preco + (preco * 0.2)
        parcela = int(input('Total de parcelas: '))
        preco_final = total / parcela
        print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcela, preco_final))
    else:
        print('Escolha uma opção válida.')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
