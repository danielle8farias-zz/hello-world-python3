'''
Pedir ao usuário para digitar a data completa do nascimento.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('data completa do nascimento')

dia = input('Digite o dia do seu nascimento: ').upper().strip()
mes = input('Digite o mês do seu nascimento: ').upper().strip()
ano = input('Digite o ano do seu nascimento: ').upper().strip()
print()
print('Você nasceu no dia {} de {} de {}.'.format(dia, mes, ano))

rodape()
