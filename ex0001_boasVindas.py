#!/usr/bin/env python3.7
'''
Leia um nome e mostre uma mensagem de boas-vindas
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('mensagem de boas vindas')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #upper: joga a string para maiúsculo
    #strip: remove os espaços no começo e no fim
    nome = input('Qual o seu nome? ').upper().strip()
    print(f'Seja bem-vindo {nome}!')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N]? ').upper().strip()[0]
    if resposta == 'N':
        #quebrando o 1º laço
        break
    print()
rodape()
