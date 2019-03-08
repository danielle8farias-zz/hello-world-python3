'''
Leia um número inteiro e mostre a sequência de Fibonacci dos n elementos lidos.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('SEQUÊNCIA FIBONACCI')

n = int(input('Quantos termos você quer mostrar? '))
n1 = 1
n2 = 1
print('~'*30)
print('{} - {} - '.format(n1, n2), end='')
cont = 3 #porque começa do terceiro termo
while cont <= n:
    fib = n1 + n2
    n1 = n2
    n2 = fib
    cont += 1
    print('{} - '.format(fib), end='')
print()

rodape()
