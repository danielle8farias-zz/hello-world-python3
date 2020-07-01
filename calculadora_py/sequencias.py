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
    

def pa():
    A1 =  float(input('Primeiro termo: '))
    r = float(input('Razão: '))
    i = 1
    An = A1
    termo = 10
    total_termos = 10
    while termo != 0:
        while termo > 0:
            print(f'{An:.2f}', end=' -> ')
            An = A1 + i*r
            i += 1
            termo -= 1
        print('pausa')
        print('Digite 0 para encerrar.')
        termo = int(input('Quantos termos deseja mostrar? '))
        total_termos += termo
    print(f'Total de termos mostrados: {total_termos}\n')

