import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int

from time import sleep


def bases():
    ler_cabecalho('BASES BINÁRIA, OCTAL E HEXADECIMAL')
    num = ler_num_int('Digite um número inteiro: ')
    sleep(0.5)
    print(f'Em binário: {bin(num)[2:]}')
    sleep(0.5)
    print(f'Em octal: {oct(num)[2:]}')
    sleep(0.5)
    print(f'Em hexadecimal: {hex(num)[2:]}')
    sleep(0.5)
    print()
