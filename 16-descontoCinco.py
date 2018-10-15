'''
Leia o valor e desconte 5%.
'''
print('-'*50)
print('{: ^50}'.format('DESCONTO 5%'))
print('-'*50)
preco = float(input('Digite o preço: R$'))
desconto = preco - (preco*0.05)
print('O novo preço com desconto de 5% é R${:.2f}'.format(desconto))
