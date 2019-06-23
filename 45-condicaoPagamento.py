'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e a condição de pagamento.
à vista dinheiro ofereça desconto de 10%
à vista no cartão ou cheque ofereça desconto de 5%
2x no cartão, preço normal
3x ou mais, 20% de juros
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que escolhe e calcula o tipo de pagamento
def tipo_pagamento(opcao):
    if opcao == 1:
        total = preco - (preco * 0.1)
        #:.2f limita o número de duas casas decimais
        print(f'Sua compra vai custar R${total:.2f}')
    elif opcao == 2:
        total = preco - (preco * 0.05)
        print(f'Sua compra vai custar R${total:.2f}')
    elif opcao == 3:
        total = preco/2
        print(f'Sua compra será parcelada em 2x de R${total:.2f}')
    elif opcao == 4:
        total = preco + (preco * 0.2)
        parcela = int(input('Total de parcelas: '))
        #tratando as parcelas para essa opção
        while parcela <= 2:
            print('Valor inválido! Apenas parcelas acima de 2 nessa opção.')
            parcela = int(input('Digite novamente. Total de parcelas: '))
            if parcela >= 3:
                break
        preco_final = total / parcela
        print(f'Sua compra será parcelada em {parcela}x de R$ {preco_final:.2f} com juros')
    else:
        print('Escolha uma opção válida.')

#programa principal
cabecalho('formas de pagamento')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    preco =  float(input('Preço das compras: R$ '))
    print('''Escolha como vai pagar:
    [1] à vista dinheiro.
    [2] à vista cartão/cheque
    [3] 2x no cartão de crédito
    [4] 3x ou mais no cartão''')
    opcao = int(input('Qual é a opção? '))
    tipo_pagamento(opcao)
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
