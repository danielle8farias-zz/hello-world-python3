'''
Leia um float e retorne a parte inteira usando arredondamento se necessário.
'''
print('-'*50)
print('{: ^50}'.format('PARTE INTEIRA COM ARREDONDAMENTO'))
print('-'*50)
while True:
    num = float(input('Digite um número: '))
    print()
    print('A parte inteira do número é {:.0f}'.format(num))
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
