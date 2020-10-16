########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Menu inicial do jogo com os temas a serem escolhidos.
#           Desenho da forca.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_nat

#criando menu e retornando opção escolhida
def escolher_tema(lista_temas):
    '''
    Cria o menu e retorna a opção escolhida
    '''
    c = 1
    for item in lista_temas:
        print(f'{c} - {item}')
        c += 1
    print()
    opcao = ler_num_nat('Escolha um tema: ')
    return opcao


def desenhar_forca():
    '''
    Sequência do desenho do bonequinho na forca
    '''
    desenho = ['''
    +----+
    |    |
    |
    |
    |
    |
    |
    ===========''',
    '''
    +----+
    |    |
    |    O
    |
    |
    |
    |
    ===========''',
    '''
    +----+
    |    |
    |    O
    |    |
    |
    |
    |
    ===========''',
    '''
    +----+
    |    |
    |    O
    |   /|
    |
    |
    |
    ===========''',
    '''
    +----+
    |    |
    |    O
    |   /|\\
    |
    |
    |
    ===========''',
    '''
    +----+
    |    |
    |    O
    |   /|\\
    |   / 
    |
    |
    ===========''',
    '''
    +----+
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    |
    ===========   
    ''']
    return desenho
