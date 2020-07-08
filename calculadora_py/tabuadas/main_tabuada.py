import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float, ler_num_int

#importando pacote de tabuadas
from tabuadas.tabuada_soma import tab_somar
from tabuadas.tabuada_subtracao import tab_subtrair
from tabuadas.tabuada_multiplicacao import tab_multiplicar
from tabuadas.tabuada_divisao import tab_dividir

from time import sleep
   

def tipo_tabuada():
    ler_cabecalho('tabuadas')
    num = ler_num_float('Digite um número: ')
    print('''
    0- sair
    1- tabuada de somar
    2- tabuada de subtrair
    3- tabuada de multiplicar
    4- tabuada de dividir
    ''')
    opcao = ler_num_int('Escolha uma das opções: ')
    print()

    if opcao == 1:
        tab_somar(num)
    elif opcao == 2:
        tab_subtrair(num)
    elif opcao == 3:
        tab_multiplicar(num)
    elif opcao == 4:
        tab_dividir(num)
    else:
        pass
