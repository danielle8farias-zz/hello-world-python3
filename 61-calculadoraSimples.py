#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha

#programa principal
cabecalho('calculadora simples')
num1 = int(input('Digite o 1º número inteiro: '))
num2 = int(input('Digite o 2º número inteiro: '))
linha()
print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
''')
opcao = int(input('Escolha uma das opções: '))
#inicializando o resultado
resultado = 0
while opcao != 5:
    if opcao == 1:
        resultado = num1 + num2
        print(f'A soma é: {resultado}')
    elif opcao == 2:
        resultado = num1 * num2
        print(f'A multiplicação é: {resultado}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior é {num1}')
        else:
            print(f'O maior é {num2}')
    elif opcao == 4:
        print('Quais são os números novamente:')
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
    else:
        print('Opção inválida. Tente novamente.')
    linha()
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    ''')
    opcao = int(input('Escolha uma das opções: '))
rodape()
