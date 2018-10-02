num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
print('=-'*20)
print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
''')
opcao = int(input('Escolha uma das opções: '))
resultado = 0
while opcao != 5:
    if opcao == 1:
        resultado = num1 + num2
        print('A soma é: {}'.format(resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('A multiplicação é: {}'.format(resultado))
    elif opcao == 3:
        if num1 > num2:
            print('O maior é {}'.format(num1))
        else:
            print('O maior é {}'.format(num2))
    elif opcao == 4:
        print('Quais são os números novamente:')
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
    else:
        print('Opção inválida. Tente novamente.')
    print('=-'*20)
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    ''')
    opcao = int(input('Escolha uma das opções: '))
