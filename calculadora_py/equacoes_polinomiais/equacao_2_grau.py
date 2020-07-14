import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_float

from math import pow
from time import sleep


def calcular_delta(a, b, c):
    delta = (pow(b, 2)) - 4 * a * c
    sleep(0.5)
    print(f'Delta: {delta}')


def equacao_seg_grau():
    a = ler_num_float('Valor de a: ')
    b = ler_num_float('Valor de b: ')
    c = ler_num_float('Valor de c: ')

    calcular_delta(a, b, c)
