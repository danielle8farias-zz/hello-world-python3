import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float, ler_num_int

from math import sqrt, hypot
from time import sleep


def calcular_cateto(a, b):
    c = sqrt(a**2 - pow(b, 2))
    return c


def hipo():
    ler_cabecalho('lados de um triângulo retângulo')
    sleep(0.5)
    print('''
    0- sair
    1- hipotenusa
    2- cateto
    '''
    )
    escolha = ler_num_int('O que deseja calcular? ')
    print()
    if escolha == 1:
        b = ler_num_float('Digite o 1º Cateto: ')
        c = ler_num_float('Digite o 2º Cateto: ')
        #a = sqrt(b**2 + c**2)
        a = hypot(b, c)
        sleep(0.5)
        print(f'O valor da Hipotenusa é: {a:.2f}')
    elif escolha == 2:
        a = ler_num_float('Digite a Hipotenusa: ')
        b = ler_num_float('Digite o Cateto: ')
        c = calcular_cateto(a, b)
        sleep(0.5)
        print(f'O valor do outro Cateto é: {c:.2f}')
    else:
        pass
    print()
