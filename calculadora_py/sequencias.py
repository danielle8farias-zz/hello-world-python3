import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_nat, ler_num_float


def fatorial():
    ler_cabecalho('fatorial')
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
    ler_cabecalho('progressão aritmética')
    A1 =  ler_num_float('Primeiro termo: ')
    r = ler_num_float('Razão: ')
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
        termo = ler_num_nat('Quantos termos deseja mostrar? ')
        total_termos += termo
    print(f'Total de termos mostrados: {total_termos}\n')


def fibo():
    ler_cabecalho('sequência fibonacci')
    num = ler_num_nat('Quantos termos você quer mostrar? ')
    if num == 1:
        print('0')
    elif num > 0:
        t1 = 0
        t2 = 1
        print(f'{t1} -> {t2}', end='')
        i = 3
        while i <= num:
            tn = t1 + t2
            print(f' -> {tn}', end='')
            t1 = t2
            t2 = tn
            i += 1
    print()

