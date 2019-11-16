'''
Crie um programa com apenas uma tupla, com nomes de produtos e seus respectivos
preços.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('TABELA DE PREÇOS')

lista = ('lápis', 1.25,
        'borracha', 0.5,
        'caderno', 12.90,
        'mochila', 35.70,
        'estojo', 11,
        'caneta', 2.99,
        'régua', 0.99)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R$ {lista[i]:>4.2f}')

rodape()
