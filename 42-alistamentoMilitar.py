'''
Informe o ano de nascimento e retorne se o usuário precisa se alistar e
quanto tempo falta.
'''
from mensagem import cabecalho
from mensagem import rodape
from datetime import date

cabecalho('ALISTAMENTO MILITAR')

atual = date.today().year
while True:
    nasc = int(input('Seu ano de nascimento: '))
    idade = atual - nasc
    print('Sua idade é {} anos'.format(idade))
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos.')
        print('Faltam {} anos para seu alistamento.'.format(saldo))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
