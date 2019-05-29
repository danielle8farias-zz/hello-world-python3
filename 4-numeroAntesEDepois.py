'''
Escolha um número e mostre seu anterior e sucessor.
'''
from mensagem import cabecalho
from mensagem import rodape

def ant_suc(num):
    ant = num - 1
    suc = num + 1
    return ant, suc

#programa principal
cabecalho('NÚMERO ANTERIOR E SUCESSOR')
while True:
    num = int(input('Escreva um número: '))
    ant, suc = ant_suc(num)
    print()
    print(f'O antecessor é {ant} e o sucessor {suc}.')
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
rodape()
