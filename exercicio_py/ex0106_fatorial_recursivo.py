'''
Usuário digita um número natural e programa retorna o seu fatorial; usando recursão.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape
from numeros import ler_num_nat


def fat(n):
    if n == 1 or n == 0:
        return 1
    return fat(n-1) * n

ler_cabecalho('calculando o fatorial')
num = ler_num_nat('Digite um número: ')
print(fat(num))
rodape()
