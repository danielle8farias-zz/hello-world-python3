'''
Digite um número e mostro o dobro, o triplo e a raiz quadrada.
'''
print('-'*50)
print('{: ^50}'.format('DOBRO, TRIPLO E RAÍZ QUADRADA'))
print('-'*50)
num = float(input('Digite um número: '))
dobro = num*2
print('O dobro de {} é {}'.format(num, dobro))
triplo = num*3
print('O triplo de {} é {}'.format(num, triplo))
raiz = num**(1/2)
print('A raiz quadrada de {} é {}'.format(num, raiz))
