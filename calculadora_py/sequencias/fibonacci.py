import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_nat


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

