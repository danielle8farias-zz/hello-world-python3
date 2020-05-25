'''
Usuário digita um valor em dinheiro e programa retorna as condições de pagamento: 
para pagamento à vista em dinheiro há um desconto de 10%;
para pagamento à vista no cartão ou cheque há um desconto de 5%;
para pagamento de 2x no cartão, o preço é normal;
para pagamento de 3x ou mais, há 20% de juros.
'''

preco =  float(input('Valor das compras: R$ '))
print()

print('''Escolha como vai pagar:
[1] à vista dinheiro.
[2] à vista cartão/cheque
[3] 2x no cartão de crédito
[4] 3x ou mais no cartão''')
opcao = int(input())
print()

if opcao == 1:
    total = preco - (preco * 0.1)
    print('Desconto de 10%.')
    print(f'Sua compra vai custar R${total:.2f}')
elif opcao == 2:
    total = preco - (preco * 0.05)
    print('Desconto de 5%.')
    print(f'Sua compra vai custar R${total:.2f}')
elif opcao == 3:
    total = preco/2
    print('Sem desconto.')
    print(f'Sua compra será parcelada em 2x de R${total:.2f}')
elif opcao == 4:
    total = preco + (preco * 0.2)
    parcela = int(input('Total de parcelas: '))
    #laço while
    #tratando as parcelas para essa opção
    #enquanto o valor de parcela for menor ou igual a 2
    while parcela <= 2:
        print('Valor inválido! Apenas parcelas acima de 2 nessa opção.')
        parcela = int(input('Digite novamente. Total de parcelas: '))
        if parcela >= 3:
            #quebrando o laço while
            break
    preco_final = total / parcela
    print(f'20% de juros!')
    print(f'Sua compra será parcelada em {parcela}x de R$ {preco_final:.2f} com juros')
    print(f'Valor total: R${total}')
else:
    print('Escolha uma opção válida.')
print()
