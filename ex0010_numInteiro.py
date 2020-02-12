#!/usr/bin/env python3.7
'''
Leia um float e retorne a parte inteira usando arredondamento se necessário.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('PARTE INTEIRA COM ARREDONDAMENTO PARA CIMA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = float(input('Digite um número com casa decimal: '))
    #python faz o arredondamento automaticamente
    #:.0f limita o número de casas decimais a zero
    print(f'A parte inteira do número é {num:.0f}')
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
