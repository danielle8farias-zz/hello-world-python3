'''
Faça a tabuada de multiplicação de vários números, um de cada vez.
O programa para quando é dado um número negativo.
'''
print('-'*50)
print('{: ^50}'.format('TABUADA'))
print('-'*50)
num = int(input('Digite um número para ver sua tabuada: '))
while num >= 0:
    print('-'*40)
    for i in range (0,11):
        multiplicacao = num * i
        print('{} * {:2} = {}'.format(num, i, multiplicacao))
    num = int(input('Digite um número para ver sua tabuada: '))
print('Programa encerrado.')
