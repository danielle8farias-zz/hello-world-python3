#!/usr/bin/env python3.7
'''
Escolha um número e mostre seu anterior e sucessor.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que retorna o número antecessor e sucessor
def ant_suc(num):
    ant = num - 1
    suc = num + 1
    #retornando dois valores
    return ant, suc

#programa principal
cabecalho('NÚMERO ANTERIOR E SUCESSOR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = int(input('Escreva um número: '))
    ant, suc = ant_suc(num)
    print()
    print(f'O antecessor é {ant} e o sucessor {suc}.')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
