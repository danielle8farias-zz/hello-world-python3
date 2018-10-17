'''
Leia o salário de um funcionário. Se for superior a R$1.250,00 calcule
o aumento de 10%. Senão, o aumento é de 15%.

'''
salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('O salário novo é R${:.2f}'.format(novo))
