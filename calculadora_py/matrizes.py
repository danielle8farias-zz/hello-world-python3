import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int, ler_num_float
from time import sleep


#efetuando a soma das matrizes
def efetuar_soma_matrizes (A, B):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    soma = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor_soma = (A[i][j] + B[i][j])
            linha.append(valor_soma)
        soma.append(linha)
    return soma


#construindo a matriz
def construir_matriz (num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = ler_num_float(f'Digite o valor A{i}{j}: ')
            linha.append(valor)
        matriz.append(linha)
    return matriz


#determina número de linhas e colunas de uma matriz
def linha_coluna ():
    num_linhas = ler_num_int('Digite o número de linhas: ')
    num_colunas = ler_num_int('Digite o número de colunas: ')
    return num_linhas, num_colunas


#chamda principal da soma de matrizes
def somar_matrizes(opcao):
    ler_cabecalho('soma duas matrizes')
    #definindo a ordem das matrizes 
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    #verificando se são de mesma ordem
    if Ai == Bi and Aj == Bj:
        #construindo as matrizes
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
        resultado = efetuar_soma_matrizes(A, B)
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


#função que verifica a validade da escolha
def ler_escolha(num):
    while True:
        try:
            escolha = int(input(num))
            #verificando se a escolha é diferente de 1 ou 2
            if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
                raise Exception('Escolha entre 1 e 4.')
        except ValueError:
            print('Digite um número.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return escolha


#primeira chamada da função
def tipo_matriz():
    ler_cabecalho('Matrizes')
    print('''
    1- Somar duas matrizes
    2- ...
    3- ...
    ''')
    opcao = ler_escolha('Escolha uma das opções: ')
    print()
    if opcao == 1:
        somar_matrizes(opcao)
        sleep(1)
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    else:
        pass
