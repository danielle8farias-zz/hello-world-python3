import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        ler_cabecalho('Pessoas cadastradas:')
        print(a.read())
    finally:
        a.close()
