#!/usr/bin/env python3.8

'''
Usuário informa um nome completo e o programa retorna se tem a palavra SILVA nele.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/exercicios-python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape

#programa principal
cabecalho('tem silva?')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #strip: remove os espaços no começo e no fim
    #lower: joga a string para maiúsculo
    nome = input('Qual seu nome completo? ').strip().lower()
    print(f'Seu nome tem Silva? {"silva" in nome}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
