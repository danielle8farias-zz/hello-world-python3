'''
Leia o ano de nascimento de um atleta e defina sua categoria de acordo com
a idade.
até 9 anos = mirim
até 14 anos = infantil
até 19 anos = júnior
até 25 anos = sênior
acima de 25 = master
'''
from mensagem import cabecalho
from mensagem import rodape
from datetime import date

cabecalho('CLASSIFICAÇÃO DE ATLETAS')

atual = date.today().year
while True:
    nasc = int(input('Digite a data de nascimento: '))
    idade = atual - nasc
    print('Sua idade é {} anos.'.format(idade))
    if idade < 10:
        print('Classificação: Mirim')
    elif idade < 15:
        print('Classificação: Infantil')
    elif idade < 20:
        print('Classificação: Júnior')
    elif idade < 26:
        print('Classificação: Sênior')
    else:
        print('Classificação: Master')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
