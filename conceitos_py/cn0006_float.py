'''
Usuário informa um número real e programa retorna a subtração entre eles.
'''

#float() converte a string passada pelo input() em número 
#   do conjunto dos Reais
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
print()

subtracao = num1 - num2
print(f'{num1} - {num2} = {subtracao}')
