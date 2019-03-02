'''
Leia o salário de um funcionário. Se for superior a R$1.250,00 calcule
o aumento de 10%. Senão, o aumento é de 15%.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('AUMENTO SALARIAL 10 OU 15%')

while True:
    salario = float(input('Salário atual do funcionário: R$'))
    if salario <= 1250:
        novo = salario + (salario * 0.15)
        print('Aumento de 15%')
    else:
        novo = salario + (salario * 0.10)
        print('Aumento de 10%')
    print('O salário novo é R${:.2f}'.format(novo))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
