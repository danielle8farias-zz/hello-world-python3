'''
Faça um conversos de Real em Dolar.
'''
real = float(input('Valor em Reais: R$'))
dolar = real/3.86
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
