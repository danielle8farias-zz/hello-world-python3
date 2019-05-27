'''
Pedir ao usuário para digitar a data completa do nascimento.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from datetime import date

#chamando a importação
cabecalho('data completa do nascimento')

# início funções
def dia():
    while True:
        #limitando o dia de 1 a 31
        dia = int(input('Digite o dia do seu nascimento: '))
        if dia > 0 and dia < 32:
            return dia
            break
        else:
            print('Digite uma data válida!')


def mes():
    while True:
        #limitando o mês de 1 a 12
        mes = int(input('Digite o mês do seu nascimento: '))
        if mes > 0 and mes < 13:
            return mes
            break
        else:
            print('Digite uma data válida!')


def ano():
    while True:
        # retirando 5 anos do ano atual
        ano_atual = date.today().year - 5
        ano = int(input('Digite o ano do seu nascimento: '))
        #limitando o ano
        if ano > 1900 and ano < ano_atual:
            return ano
            break
        else:
            print('Digite uma data válida!')


def main():
    dia_info = dia()
    mes_info = mes()
    ano_info = ano()
    print()
    print(f'Você nasceu no dia {dia_info} de {mes_info} de {ano_info}.')
#fim das funções


#programa principal
main()

#chamando a importação
rodape()
