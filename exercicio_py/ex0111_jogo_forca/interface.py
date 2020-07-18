import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_nat


#criando menu e retornando opção escolhida
def escolher_tema(lista_temas):
    c = 1
    for item in lista_temas:
        print(f'{c} - {item}')
        c += 1
    print()
    opcao = ler_num_nat('Escolha um tema: ')
    return opcao


def desenhar_forca():
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
    for i in desenho:
        print(i)
