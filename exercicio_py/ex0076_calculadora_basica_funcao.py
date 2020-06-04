'''
Calculadora básica que soma, subtrai, multiplica ou divide dois números. 
Usando funções.
'''

from time import sleep

def criar_linhas():
    print('-'*50)


def titulo(msg):
    print(f'{msg:^50}')


def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


criar_linhas()
titulo('calculadora básica')
criar_linhas()

while True:
    print('''Digite:

    1- somar
    2- subtrair
    3- multiplicar
    4- dividir
    5- sair
    ''')

    opcao = int(input('Que operação deseja realizar? '))
    print()

    if opcao == 1:
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
        soma = somar(num1, num2)
        print(f'\n{num1} + {num2} = {soma}\n')
    
    elif opcao == 2:
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
        sub = subtrair(num1, num2)
        print(f'\n{num1} - {num2} = {sub}\n')
    
    elif opcao == 3:
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
        mult = multiplicar(num1, num2)
        print(f'\n{num1} x {num2} = {mult}\n')

    elif opcao == 4:
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
        div = dividir(num1, num2)
        print(f'\n{num1} / {num2} = {div}\n')

    else:
        print('finalizando...')
        sleep(1)
        break

    sleep(2)
