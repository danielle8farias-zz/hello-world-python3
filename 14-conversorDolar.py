'''
Faça um conversos de Real em Dolar.
'''
print('-'*50)
print('{: ^50}'.format('CONVERSOR REAL EM DOLAR'))
print('-'*50)
real = float(input('Valor em Reais: R$'))
dolar = real/3.86
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
