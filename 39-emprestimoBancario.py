'''
Escreva um programa para aprovação de empréstimo bancário para compra de uma
casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
vai pagar. A prestação será negada se exceder 30% do salário do comprador.
'''
print('  Programa de Aprovação de Empréstimo  ')
valor_casa = float(input('Digite o valor da casa que deseja comprar: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao_mensal = valor_casa / (anos * 12)
print('O valor da prestação mensal será de R${:.2f}'.format(prestacao_mensal))
if prestacao_mensal < (salario * 0.3):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')
