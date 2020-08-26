import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float


def montar_equacao(x1, x2):
    b = somar_raizes(x1, x2)
    c = multip_raizes(x1, x2)

    if b < 0 and c > 0:
        print(f'A equação é: X² + {b*-1}X + {c}')
    elif b < 0  and c < 0:
        print(f'A equação é: X² + {b*-1}X - {c*-1}')
    elif b < 0  and c == 0:
        print(f'A equação é: X² + {b*-1}X')
    
    elif b > 0 and c > 0:
        print(f'A equação é: X² - {b}X + {c}')
    elif b > 0 and c < 0:
        print(f'A equação é: X² - {b}X - {c*-1}')
    elif b > 0 and c == 0:
        print(f'A equação é: X² - {b}X')
    
    elif b == 0 and c > 0:
        print(f'A equação é: X² + {c}')
    elif b == 0 and c < 0:
        print(f'A equação é: X² - {c*-1}')
    #elif b == 0 and c == 0:
    else:
        print(f'A equação é: X²')


def multip_raizes(x1, x2):
    return x1 * x2


def somar_raizes(x1, x2):
    return x1 + x2


def raizes():
    ler_cabecalho('determinar equação do 2º grau')
    x1 = ler_num_float('X1: ')
    x2 = ler_num_float('X2: ')
    montar_equacao(x1, x2)
