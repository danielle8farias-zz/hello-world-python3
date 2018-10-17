'''
Leia o salário e o aumente em 15%.
'''
print('-'*50)
print('{: ^50}'.format('SALÁRIO AUMENTO 5%'))
print('-'*50)
salario = float(input('Escreva o salário: R$'))
novo_salario = salario + salario*0.15
print('O novo salário com aumento de 15% é {:.2f}'.format(novo_salario))
