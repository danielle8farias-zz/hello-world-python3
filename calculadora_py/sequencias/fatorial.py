import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_nat

from time import sleep


def fatorial():
    ler_cabecalho('fatorial')
    num = ler_num_nat('Digite um número natural: ')
    print()
    print(f'Calculando {num}!')
    i = num
    f = 1
    while i > 0:
        if i > 1:
            print(f'{i} x ', end='', flush=True)
            sleep(0.5)
        else:
            print(f'{i} = ', end='', flush=True)
            sleep(0.5)
        f *= i
        i -= 1
    sleep(0.5)
    print(f)
    return f
