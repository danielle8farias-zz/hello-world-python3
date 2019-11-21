'''
Crie um programa com apenas uma tupla, com nomes de produtos e seus respectivos
preços.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('TABELA DE PREÇOS')
#tupla
lista = ('lápis', 1.25,
        'borracha', 0.5,
        'caderno', 12.90,
        'mochila', 35.70,
        'estojo', 11,
        'caneta', 2.99,
        'régua', 0.99)
for i in range(0, len(lista)):
    #pegando os itens da tupla de índice par: os nomes
    if i % 2 == 0:
        #.<30 trinta pontos alinhados à esquerda
        print(f'{lista[i]:.<30}', end='')
    #pegando os itens da tupla de índice impar: os preços
    else:
        #>4 alinhado à direita com 4 posições
        #.2f com duas casas decimais
        print(f'R$ {lista[i]:>5.2f}')
rodape()
