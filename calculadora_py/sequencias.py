import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_nat


def fatorial():
    num = ler_num_nat('Digite um número natural: ')
    print()
    print(f'Calculando {num}!')
    i = num
    f = 1
    while i > 0:
        if i > 1:
            print(f'{i} x ', end='')
        else:
            print(f'{i} = ', end='')
        f *= i
        i -= 1
    print(f)
    return f
    
