'''
Escolha um número e mostre seu anterior e sucessor.
'''
print('-'*50)
print('{: ^50}'.format('NÚMERO ANTERIOR E SUCESSOR'))
print('-'*50)
while True:
    num = int(input('Escreva um número: '))
    ant = num - 1
    suc = num + 1
    print()
    print('O antecessor é {} e o sucessor {}.'.format(ant,suc))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
