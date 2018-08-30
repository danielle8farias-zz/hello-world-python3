'''
Leia 3 números e mostre o maior e o menor entre eles.
'''
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 >= num2 >= num3:
    print("O maior número é",num1,"e o menor é",num3)
elif num1 >= num3 >= num2:
    print("O maior número é",num1,"e o menor é",num2)
elif num2 >= num1 >= num3:
    print("O maior número é",num2,"e o menor é",num3)
elif num2 >= num3 >= num1:
    print("O maior número é",num2,"e o menor é",num1)
elif num3 >= num1 >= num2:
    print("O maior número é",num3,"e o menor é",num2)
else:
    print("O maior número é",num3,"e o menor é",num1)

