import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_nat, ler_num_float

from time import sleep


def pa():
    ler_cabecalho('progressão aritmética')
    A1 =  ler_num_float('Primeiro termo: ')
    r = ler_num_float('Razão: ')
    i = 1
    An = A1
    termo = 10
    total_termos = 10
    while termo != 0:
        while termo > 0:
            print(f'{An:.2f}', end=' -> ', flush=True)
            An = A1 + i*r
            i += 1
            termo -= 1
            sleep(0.5)
        print('pausa')
        print('Digite 0 para encerrar.')
        termo = ler_num_nat('Quantos termos deseja mostrar? ')
        total_termos += termo
    print(f'Total de termos mostrados: {total_termos}\n')
