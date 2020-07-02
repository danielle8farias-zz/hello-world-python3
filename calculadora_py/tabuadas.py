import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int, ler_num_float

from time import sleep

def tab_somar(n):
    ler_cabecalho('tabuada de soma')
    for i in range(1, 10):
        print(f'{n:4} + {i} = {n+i}')
        sleep(0.5)


def tab_subtrair(n):
    ler_cabecalho('tabuada de subtração')
    for i in range(1, 10):
        print(f'{n:4} - {i} = {n-i}')
        sleep(0.5)


def tab_multiplicar(n):
    ler_cabecalho('tabuada de multiplicação')
    for i in range(1, 10):
        print(f'{n:4} x {i} = {n*i}')
        sleep(0.5)


def tab_dividir(n):
    ler_cabecalho('tabuada de divisão')
    for i in range(1, 10):
        print(f'{n:4} / {i} = {n/i:.2f}')
        sleep(0.5)


#função que verifica a validade da escolha
def ler_escolha(num):
    while True:
        try:
            escolha = int(input(num))
            #verificando se a escolha é diferente de 1 ou 2
            if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
                raise Exception('Escolha entre 1 e 4.')
        except ValueError:
            print('Digite um número.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return escolha

        

def tipo_tabuada():
    ler_cabecalho('tabuadas')
    num = ler_num_float('Digite um número: ')
    print('''
    1- tabuada de somar
    2- tabuada de subtrair
    3- tabuada de multiplicar
    4- tabuada de dividir
    ''')
    opcao = ler_escolha('Escolha uma das opções: ')
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

