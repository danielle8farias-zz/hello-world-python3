'''
Faça um programa que compare dois números.
'''
num1 = int (input("Digite o 1º número: "))
num2 = int (input("Digite o 2º número: "))

if num1 > num2:
    print("O maior número é",num1)
elif num2 > num1:
    print("O maior número é:",num2)
else:
    print('Os valores são iguais.')
