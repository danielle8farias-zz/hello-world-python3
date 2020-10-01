#!/usr/bin/env python3.8

'''
Abrindo, lendo um arquivo com tratamento de exceções. Caso o arquivo não exista, ele será criado.
'''

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
        print('houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())


arquivo = 'numero.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)
else:
    ler_arquivo(arquivo)
