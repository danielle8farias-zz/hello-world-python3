from time import sleep

def tab_somar(n):
    for i in range(1, 10):
        print(f'{n:4} + {i} = {n+i}')
        sleep(0.5)


def tab_subtrair(n):
    for i in range(1, 10):
        print(f'{n:4} - {i} = {n-i}')
        sleep(0.5)


def tab_multiplicar(n):
    for i in range(1, 10):
        print(f'{n:4} x {i} = {n*i}')
        sleep(0.5)


def tab_dividir(n):
    for i in range(1, 10):
        print(f'{n:4} / {i} = {n/i:.2f}')
        sleep(0.5)
        

def tipo_tabuada():
    num = float(input('Digite um número: '))
    print('''
    1- tabuada de somar
    2- tabuada de subtrair
    3- tabuada de multiplicar
    4- tabuada de dividir
    ''')
    opcao = int(input('Escolha uma das opções: '))
    print()

    if opcao == 1:
        tab_somar(num)
    elif opcao == 2:
        tab_subtrair(num)
    elif opcao == 3:
        tab_multiplicar(num)
    elif opcao == 4:
        tab_dividir(num)
    else:
        pass
