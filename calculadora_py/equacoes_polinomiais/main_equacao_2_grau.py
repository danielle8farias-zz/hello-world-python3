import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int

from equacoes_polinomiais.raizes_equacao_2_grau import equacao_seg_grau
from equacoes_polinomiais.determina_equacao_2_grau import raizes


def equacoes():
    ler_cabecalho('equação do 2º grau')
    print('''
    0- sair
    1- determinar raízes de uma equação do 2º grau
    2- determinar a equação do 2º grau com a entrada das raízes
    ''')
    opcao = ler_num_int('Escolha uma das opções: ')
    print()
    if opcao == 1:
        equacao_seg_grau()
    elif opcao == 2:
        raizes()
    else:
        pass
