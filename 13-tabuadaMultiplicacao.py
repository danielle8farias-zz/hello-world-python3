'''
Faça a tabuada de multiplicação de um número dado.
'''
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(0,11):
    multiplicacao = num * i
    print('{} * {:2} = {}'.format(num, i, multiplicacao))
