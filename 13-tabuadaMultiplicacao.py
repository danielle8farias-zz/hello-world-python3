'''
Faça a tabuada de multiplicação de vários números, um de cada vez.
O programa para quando é dado um número negativo.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('TABUADA')

print('Para encerrar digite um número negativo')
num = int(input('Digite um número para ver sua tabuada: '))
while num >= 0:
    print('-'*40)
    for i in range (0,11):
        multiplicacao = num * i
        print('{} * {:2} = {}'.format(num, i, multiplicacao))
    num = int(input('Digite um número para ver sua tabuada: '))

rodape()
