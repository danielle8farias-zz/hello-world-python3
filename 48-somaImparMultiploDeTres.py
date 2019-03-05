'''
Soma dos números ímpares múltiplos de 3 até 500.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('Soma dos números ímpares múltiplos de 3 até 500')

soma = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        print(n, end=' ')
        soma += n
print('\nA soma desses números é {}.'.format(soma))

rodape()
