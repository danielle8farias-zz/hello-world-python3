########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o salário de uma pessoa. 
# O programa retorna um reajuste de aumento desse salário.
# Se o salário for superior a R$1.250,00 o aumento deve ser de 10%; senão o aumento é de 15% 
########

salario = float(input('Salário atual do funcionário: R$'))

#verificando se salário é menor ou igual a R$1.250,00
if salario <= 1250:
    novo = salario + (salario * 0.15)
    print('Aumento de 15%')
else:
    novo = salario + (salario * 0.10)
    print('Aumento de 10%')
#print() fora da condicional
print(f'O salário novo é R${novo:.2f}\n')
