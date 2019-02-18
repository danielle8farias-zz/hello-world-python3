'''
Escolha um número e mostre seu anterior e sucessor.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('NÚMERO ANTERIOR E SUCESSOR')

while True:
    num = int(input('Escreva um número: '))
    ant = num - 1
    suc = num + 1
    print()
    print('O antecessor é {} e o sucessor {}.'.format(ant,suc))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break

rodape()
