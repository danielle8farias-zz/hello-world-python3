import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_float

from math import pow, sqrt
from time import sleep


def calcular_raizes(a, b, raiz_delta):
    x1 = (-b + raiz_delta)/(2 * a)
    x2 = (-b - raiz_delta)/(2 * a)
    print(f'Raizes: {x1} e {x2}')


def calcular_raiz_delta(a, b, delta):
    raiz_delta = sqrt(delta)
    sleep(0.5)
    print(f'Raiz quadrada de Delta: {raiz_delta:.4f}')
    calcular_raizes(a, b, raiz_delta)


def calcular_delta(a, b, c):
    delta = (pow(b, 2)) - 4 * a * c
    sleep(0.5)
    print(f'Delta: {delta}')
    calcular_raiz_delta(a, b, delta)


def tratar_a(n):
    while True:
        try:
            a = float(input(n))
            if a == 0:
                raise Exception('Deve ser um número diferente de zero.')
        except ValueError:
            print('Digite um valor para a.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return a


def equacao_seg_grau():
    a = tratar_a('Valor de a: ')
    b = ler_num_float('Valor de b: ')
    c = ler_num_float('Valor de c: ')

    calcular_delta(a, b, c)
