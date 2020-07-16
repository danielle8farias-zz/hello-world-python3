'''
Abrindo uma matriz de um arquivo e mostrando seus elementos na tela.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta

from time import sleep


#função que imprime matriz
def imprimir_matriz(matriz):
    #percorrendo as linhas
    for i in range(len(matriz)):
        sleep(0.5)
        #percorrendo as colunas
        for j in range(len(matriz[0])):
            print(f'[{matriz[i][j]:^7}]', end='', flush=True)
        print()


def lendo_matriz(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO! Não foi possível abrir o arquivo')
    else:
        matriz = []
        linha = a.readline()
        while linha != "":
            elementos = linha.split()
            for i in range(len(elementos)):
                elementos[i] = float(elementos[i])
            matriz.append(elementos)
            linha = a.readline()
        a.close()
        imprimir_matriz(matriz)


ler_cabecalho('abrindo matriz de um arquivo')
arquivo = 'matriz4x5.txt'
lendo_matriz(arquivo)
rodape()
