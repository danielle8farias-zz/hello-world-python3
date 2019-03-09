'''Calcula o aumento de salário dado o valor e a porcentagem'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('AUMENTO DE SALÁRIO')

while True:
    salario = float(input('Salário: R$ '))
    porcentagem = float(input('Porcentagem de aumento: '))
    aumento = salario * porcentagem/100
    salario = salario + aumento
    print('O aumento foi de R$ {:.2f}'.format(aumento))
    print('O novo salário é R$ {:.2f}'.format(salario))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
