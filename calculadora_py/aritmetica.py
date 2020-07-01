import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_float, ler_divisor, ler_num_int, ler_indice


def somar():
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    return num1 + num2


def subtrair():
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    return num1 - num2


def multiplicar():
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    return num1 * num2


def dividir():
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_divisor('Digite o 2º número: ')
    return num1 / num2


from math import pow
def exponenciar():
    base = ler_num_float('Digite o número da base: ')
    expo = ler_num_int('Digite o número do expoente: ')
    return pow(base, expo)


def radiciar():
    indice = ler_indice('Índice da raiz: ')
    radicando = ler_num_float('Radicando: ')
    if indice % 2 == 0 and radicando >= 0:
        raiz = radicando ** (1/indice)
        return raiz
    elif radicando < 0 and indice % 2 == 1:
        radicando *= -1
        raiz = radicando ** (1/indice)
        return raiz * -1
    else:
        return 'Não é possível calcular a raiz dentro dos Reais.'
    