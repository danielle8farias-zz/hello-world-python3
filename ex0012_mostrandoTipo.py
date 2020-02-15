#!/usr/bin/env python3.7
'''
Digite algo e mostre a tipagem da mesma.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('TIPO DE DADO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    a = input('Digite algo: ')
    print('O tipo primitivo desse valor é', type(a))
    print('Só tem espaços?', a.isspace())
    print('É um número?', a.isnumeric())
    print('É composto de letras?', a.isalpha())
    print('Ele é alfanumérico?', a.isalnum())
    print('Está em maiúsculas?', a.isupper())
    print('Está em minúsculas?', a.islower())
    print('Está capitalizada?', a.istitle())
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
