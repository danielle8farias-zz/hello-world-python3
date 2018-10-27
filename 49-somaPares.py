'''
Leia 6 números inteiros e mostre a soma daqueles que são pares.
'''
print('-'*50)
print('{: ^50}'.format('SOMA DE NÚMEROS PARES'))
print('-'*50)
while True:
    soma = 0
    for i in range(1,7):
        num = int(input('Digite o {}º número: '.format(i)))
        if num % 2 == 0:
            soma += num
    print('A soma dos números pares é {}.'.format(soma))
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
