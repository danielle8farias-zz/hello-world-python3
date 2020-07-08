import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float, ler_num_int


from math import pow
def exponenciar():
    ler_cabecalho('exponenciação')
    base = ler_num_float('Digite o número da base: ')
    expo = ler_num_int('Digite o número do expoente: ')
    return pow(base, expo)
