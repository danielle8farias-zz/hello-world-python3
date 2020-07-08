import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float, ler_indice


def radiciar():
    ler_cabecalho('radiciação')
    indice = ler_indice('Índice da raiz: ')
    radicando = ler_num_float('Radicando: ')
    if indice % 2 == 0 and radicando >= 0:
        raiz = radicando ** (1/indice)
        return raiz
    elif radicando < 0 and indice % 2 == 1:
        radicando *= -1
        raiz = radicando ** (1/indice)
        return raiz * -1
    else:
        return 'Não é possível calcular a raiz dentro dos Reais.'
