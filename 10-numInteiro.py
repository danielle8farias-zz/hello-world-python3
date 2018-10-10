'''
Leia um float e retorne a parte inteira sem qualquer tipo de arredondamento.
'''
print('-'*50)
print('{: ^50}'.format('PARTE INTEIRA SEM ARREDONDAMENTO'))
print('-'*50)
num = float(input('Digite um número: '))
print('A parte inteira do número é {:.0f}'.format(num))
