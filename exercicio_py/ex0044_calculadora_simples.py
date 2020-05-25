'''
Calculadora simples, com operação de 
soma, subtração, multiplicação e divisão de 2 números.
'''

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
opcao = 0

while opcao != 5:
    print('''
Selecione uma operação:
[1] somar
[2] subtrair
[3] multiplicar
[4] dividir
[5] sair''')
    opcao = int(input())
    print()

    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif opcao == 3:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif opcao == 4:
        print(f'{num1} / {num2} = {num1 / num2}')
    elif opcao == 5:
        print('saindo do programa...')
        break
    else:
        print('Valor inválido!')

print('FIM')
