import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho

from time import sleep


def tab_subtrair(n):
    ler_cabecalho('tabuada de subtração')
    for i in range(1, 10):
        print(f'{n:4} - {i} = {n-i}')
        sleep(0.5)
    print()
