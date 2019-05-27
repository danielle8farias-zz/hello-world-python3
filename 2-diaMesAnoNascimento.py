'''
Pedir ao usuário para digitar a data completa do nascimento.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#chamando a importação
cabecalho('data completa do nascimento')

def dia():
    while True:
        #limitando o dia de 1 a 31
        dia = input('Digite o dia do seu nascimento: ').upper().strip()
        if 0 > dia < 32:
            return dia
            break
        else:
            print('Digite uma data válida!')


mes = input('Digite o mês do seu nascimento: ').upper().strip()
ano = input('Digite o ano do seu nascimento: ').upper().strip()
print()
print(f'Você nasceu no dia {dia()} de {mes} de {ano}.')

#chamando a importação
rodape()
