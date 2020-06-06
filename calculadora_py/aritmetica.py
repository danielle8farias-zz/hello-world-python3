import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_float, ler_divisor


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
    base = float(input('Digite o número da base: '))
    expo = float(input('Digite o número do expoente: '))
    return pow(base, expo)


def radiciar():
    radicando = int(input('Radicando: '))
    indice = int(input('Raiz: '))
    raiz = radicando ** (1/indice)
    return raiz

#ver essa desgra de exponenciação e radiciação