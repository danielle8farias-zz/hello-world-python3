'''
Usuário informa dois números inteiros e programa retorna a divisão entre eles, a divisão inteira e o resto da divisão.
'''

num1 = int(input('Digite o 1º número inteiro: '))
num2 = int(input('Digite o 2º número inteiro: '))

#calculando divisão
divisao = num1 / num2
print(f'Resultado da divisão: {divisao}')
print()

#calculando divisão inteira
divisao_int = num1 // num2
print(f'Resultado da divisão inteira: {divisao_int}')
print()

#calculando o resto da divisão
resto_div = num1 % num2
print(f'Resultado do resto da divisão: {resto_div}')
print()
