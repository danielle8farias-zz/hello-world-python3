import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float

from time import sleep
from math import radians, sin, cos, tan


def razao_trigon():
    ler_cabecalho('SENO COSSENO TANGENTE')
    numero = ler_num_float('Digite um ângulo: ')
    #radians() convertendo float para radianos
    seno = sin(radians(numero))
    cosseno = cos(radians(numero))
    tangente = tan(radians(numero))
    sleep(0.5)
    print(f'O seno é {seno:.2f}')
    sleep(0.5)
    print(f'O cosseno é {cosseno:.2f}')
    sleep(0.5)
    print(f'A tangente é {tangente:.2f}')
    print()
