import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int

from matrizes.soma_matriz import somar_matrizes
from matrizes.subtra_matriz import subtrair_matrizes
from matrizes.multip_real_matriz import multiplicacao_real
from matrizes.multip_matrizes import multiplicacao_matriz


#primeira chamada da função
def tipo_matriz():
    ler_cabecalho('Matrizes')
    print('''
    0- sair
    1- Somar duas matrizes
    2- Subtrair duas matrizes
    3- Multiplicação de uma matriz por um número real
    4- Multiplicação de matrizes
    ''')
    opcao = ler_num_int('Escolha uma das opções: ')
    print()
    if opcao == 1:
        somar_matrizes()
    elif opcao == 2:
        subtrair_matrizes()
    elif opcao == 3:
        multiplicacao_real()
    elif opcao == 4:
        multiplicacao_matriz()
    else:
        pass
