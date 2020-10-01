#!/usr/bin/env python3.8

'''
Usuário digita, em números, a data completa de nascimento e programa retorna essa informação formatada. Com validação de dados.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
from datetime import date

def ler_mes(data_mes):
    while True:
        try:
            mes  = int(input(data_mes))
            #verificando se mês é entre 1 e 12
            if mes > 12 or mes < 1:
                raise Exception('Meses de 1 a 12.')
        except ValueError:
            print('Digite um tipo válido.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        #se o 'try' for válido
        else:
            return mes


def nome_mes(mes):
    if mes == 1:
        return 'janeiro'
    elif mes == 2:
        return 'fevereiro'
    elif mes == 3:
        return 'março'
    elif mes == 4:
        return 'abril'
    elif mes == 5:
        return 'maio'
    elif mes == 6:
        return 'junho'
    elif mes == 7:
        return 'julho'
    elif mes == 8:
        return 'agosto'
    elif mes == 9:
        return 'setembro'
    elif mes == 10:
        return 'outubro'
    elif mes == 11:
        return 'novembro'
    else:
        return 'dezembro'


#função que captura o dia informado pelo usuário do mês fevereiro
def ler_dia_fev(data_dia):
    while True:
        try:
            dia = int(input(data_dia))
            #verificando se dia é entre 1 e 28
            if dia > 28 or dia < 1:
                raise Exception('Dias de 1 a 28.')
        except ValueError:
            print('Digite um tipo válido.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return dia


#função que captura o dia informado pelo usuário do mês 31
def ler_dia_31(data_dia):
    while True:
        try:
            dia = int(input(data_dia))
            #verificando se dia é entre 1 e 31
            if dia > 31 or dia < 1:
                raise Exception('Dias de 1 a 31.')
        except ValueError:
            print('Digite um tipo válido.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return dia


#função que captura o dia informado pelo usuário do mês 30
def ler_dia_30(data_dia):
    while True:
        try:
            dia = int(input(data_dia))
            #verificando se dia é entre 1 e 30
            if dia > 30 or dia < 1:
                raise Exception('Dias de 1 a 30.')
        except ValueError:
            print('Digite um tipo válido.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return dia


#função que captura o ano informado pelo usuário
def ler_ano(data_ano):
    #date.today().year pega o ano indicado pelo sistema operacional
    #retirando 5 anos do ano atual
    ano_atual = date.today().year - 5
    while True:
        try:
            ano = int(input(data_ano))
            #limitando o ano de 1900 até o ano atual
            if ano < 1900 or ano > ano_atual:
                raise Exception(f'ano de 1900 a {ano_atual}.')
        except ValueError:
            print('Digite um tipo válido.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return ano


#programa principal
ler_cabecalho('digite a data completa do seu nascimento')
while True:
    mes = ler_mes('Mês: ')
    if mes == 2:
        dia = ler_dia_fev('Dia: ')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = ler_dia_30('Dia: ')
    else:
        dia = ler_dia_31('Dia: ')
    mes_str = nome_mes(mes)
    ano = ler_ano('Ano: ')
    print()
    print(f'Você nasceu em: {dia} de {mes_str} de {ano}')
    print()
    resposta = ler_resposta('Deseja continuar? [S/N]')
    if resposta == 'N':
        break
    else:
        linha()
        print()
rodape()
