'''
Pedir ao usuário para digitar a data completa do nascimento.
'''
print('Olá!')
print('-'*50)
dia = input('Digite o dia do seu nascimento: ').upper().strip()
mes = input('Digite o mês do seu nascimento: ').upper().strip()
ano = input('Digite o ano do seu nascimento: ').upper().strip()
print('-'*50)
print('Você nasceu no dia {} de {} de {}.'.format(dia, mes, ano))
