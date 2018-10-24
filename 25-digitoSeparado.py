'''
Leia um número de 0 a 9999 e mostre cada um dos dígitos.
'''
print('-'*50)
print('{: ^50}'.format('DÍGITOS DE UM NÚMERO'))
print('-'*50)
while True:
    num = int(input('Digite um número: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('Unidade: {}'.format(u))
    print('Dezena: {}'.format(d))
    print('Centena: {}'.format(c))
    print('Milhar: {}'.format(m))
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
