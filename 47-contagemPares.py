'''
Contagem de números pares até 50.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('CONTAGEM Nº PARES ATÉ 50')

for i in range(2, 51, 2):
    print(i, end=' ')
print()

rodape()
