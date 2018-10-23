'''
Leia o valor e desconte 5%.
'''
print('-'*50)
print('{: ^50}'.format('DESCONTO 5%'))
print('-'*50)
while True:
    preco = float(input('Digite o preço: R$'))
    desconto = preco - (preco*0.05)
    print('O novo preço com desconto de 5% é R${:.2f}'.format(desconto))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
