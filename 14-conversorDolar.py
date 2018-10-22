'''
Faça um conversos de Real em Dolar.
'''
print('-'*50)
print('{: ^50}'.format('CONVERSOR REAL EM DOLAR'))
print('-'*50)
while True:
    real = float(input('Valor em Reais: R$'))
    dolar = real/3.86
    print()
    print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
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
