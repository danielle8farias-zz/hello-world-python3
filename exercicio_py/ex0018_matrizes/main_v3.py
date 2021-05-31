########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita duas matrizes, escolhendo a ordem dessas e programa retorna a soma entre elas.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, ler_resposta
from numeros import ler_num_int, ler_num_float
from funcoes_matriz import construir_matriz, somar_matrizes
from time import sleep


def linha_coluna ():
    num_linhas = ler_num_int('Digite o número de linhas: ')
    num_colunas = ler_num_int('Digite o número de colunas: ')
    return num_linhas, num_colunas


while True:
    ler_cabecalho('soma duas matrizes')
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    if Ai == Bi and Aj == Bj:
        print('Construindo matriz A')
        A = construir_matriz(Ai, Aj)
        print('\nConstruindo matriz B')
        B = construir_matriz(Bi, Bj)
        print()
        #imprimindo as matrizes
        sleep(0.5)
        print('Matriz A:')
        for i in range(Ai):
            for j in range(Aj):
                sleep(0.5)
                print(f'[{A[i][j]:^5}]', end='', flush=True)
            print()
        print()
        sleep(0.5)
        print('Matriz B:')
        for i in range(Bi):
            for j in range(Bj):
                sleep(0.5)
                print(f'[{B[i][j]:^5}]', end='', flush=True)
            print()
        print()
        resultado = somar_matrizes(A, B)
        #imprimindo a soma
        sleep(0.5)
        print('\nResultado da soma:')
        for i in range(Ai):
            for j in range(Aj):
                sleep(0.5)
                print(f'[{resultado[i][j]:^5}]', end='', flush=True)
            print()
        print()
    else:
        print('Não é possível somar: As matrizes devem ser de mesma ordem.')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
sleep(0.5)
criar_rodape()
