#!/usr/bin/env python3.8

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

#abrir, criar ou ler arquivos não funciona no terminal do VSCode por algum motivo
