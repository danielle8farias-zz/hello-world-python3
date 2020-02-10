#!/usr/bin/env python3.7
'''
Pedir ao usuário para digitar a data completa do nascimento.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from datetime import date

#função que captura o dia informado pelo usuário
def dia():
    while True:
        dia = int(input('Digite o dia do seu nascimento: '))
        #limitando o dia de 1 a 31
        if dia > 0 and dia < 32:
            return dia
            break
        else:
            print('Digite uma data válida!')

#função que captura o mes informado pelo usuário
def mes():
    while True:
        mes = int(input('Digite o mês do seu nascimento: '))
        #limitando o mês de 1 a 12
        if mes > 0 and mes < 13:
            return mes
            break
        else:
            print('Digite uma data válida!')

#função que captura o ano informado pelo usuário
def ano():
    while True:
        #date.today().year pega o ano indicado pelo sistema operacional
        # retirando 5 anos do ano atual
        ano_atual = date.today().year - 5
        ano = int(input('Digite o ano do seu nascimento: '))
        #limitando o ano
        if ano > 1900 and ano < ano_atual:
            return ano
            break
        else:
            print('Digite uma data válida!')

#programa principal
cabecalho('data completa do nascimento')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    dia_info = dia()
    mes_info = mes()
    ano_info = ano()
    print(f'Você nasceu no dia {dia_info} de {mes_info} de {ano_info}.')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N]? ').upper().strip()[0]
    if resposta == 'N':
        #quebrando o 1º laço
        break
    print()
rodape()
