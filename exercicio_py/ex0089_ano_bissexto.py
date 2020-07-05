#!/usr/bin/env python3.8

'''
Usuário informa um ano que deseja verificar e programa retorna se esse é bissexto.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_nat


#função que calcula se o ano é bissexto
def ano_bissexto(ano):
    #verificando se o ano é divisível por 4
    #e se o ano não é divisível por 100
    #ou se o ano é divisível por 400
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} NÃO é bissexto.')


#programa principal
ler_cabecalho('ANO BISSEXTO')
while True:
    ano = ler_num_nat('Informe o ano: ')
    ano_bissexto(ano)
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
rodape()
