########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Verifica se o arquivo existe; cria o arquivo; faz a leitura e escrita do arquivo.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho

def arquivo_existe(nome):
    '''
    Verifica se o arquivo existe.
    '''
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    '''
    Cria um arquivo.
    '''
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    '''
    Faz a leitura do arquivo.
    '''
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        ler_cabecalho('Pessoas cadastradas:')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar_pessoa(arquivo, nome, idade):
    '''
    Registra a pessoa no arquivo.
    '''
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
