'''
Leia um float e retorne a parte inteira usando arredondamento se necessário.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('PARTE INTEIRA COM ARREDONDAMENTO PARA CIMA')
while True:
    num = float(input('Digite um número com casa decimal: '))
    #python faz o arredondamento automaticamente
    print(f'A parte inteira do número é {num:.0f}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
