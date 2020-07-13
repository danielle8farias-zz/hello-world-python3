import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_float


def equacao_seg_grau():
    a = ler_num_float('Valor de a: ')
    b = ler_num_float('Valor de b: ')
    c = ler_num_float('Valor de c: ')

    print(f'a:{a}, b:{b}, c:{c}')
