'''
Informe a raiz quadrada de um número inteiro.
'''
print('-'*50)
print('{: ^50}'.format('RAÍZ QUADRADA'))
print('-'*50)
from math import sqrt
while True:
    num = int(input('digite um número inteiro: '))
    raiz = sqrt(num)
    print()
    print('A raiz de {} = {}'.format(num, raiz))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
