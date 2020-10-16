########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Menu inicial do programa.
#           Mostra as opções de interação do usuário com o programa.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_int

def menu(vetor):
    c = 1
    for i in vetor:
        print(f'{c} - {i}')
        c += 1
    print()
    opcao = ler_num_int('Escolha sua opção: ')
    return opcao
