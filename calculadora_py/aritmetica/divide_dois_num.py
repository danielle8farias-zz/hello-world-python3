import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float, ler_divisor


def dividir():
    ler_cabecalho('divisão')
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_divisor('Digite o 2º número: ')
    return num1 / num2
