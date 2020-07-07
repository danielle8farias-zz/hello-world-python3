import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int, ler_num_float
from time import sleep


#efetuar multiplicação de matrizes
def efetuar_multi_matriz(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_colunas_B, num_colunas_B = len(B), len(B[0])
    multiplicacao = list()
    for i in range(num_linhas_A):
        linha = []
        for j in range(num_colunas_B):
            soma = 0
            for k in range(num_colunas_A):
                soma += A[i][k] * B[k][j]
            linha.append(soma)
        multiplicacao.append(linha)
    return multiplicacao


#efetuando multiplicação por número real
def efetuar_multi_real(A, n):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    multi_real = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = (n * A[i][j])
            linha.append(valor)
        multi_real.append(linha)
    return multi_real


#efetuando a subtração das matrizes
def efetuar_subtracao_matrizes (A, B):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    subtracao = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor_subtracao = (A[i][j] - B[i][j])
            linha.append(valor_subtracao)
        subtracao.append(linha)
    return subtracao


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


#função que imprime matriz
def imprimir_matriz(M, Mi, Mj):
    for i in range(Mi):
        for j in range(Mj):
            sleep(0.5)
            print(f'[{M[i][j]:^5}]', end='', flush=True)
        print()


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


#chamada principal da soma de matrizes
def somar_matrizes():
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
        imprimir_matriz(A, Ai, Aj)
        print()
        sleep(0.5)
        print('Matriz B:')
        imprimir_matriz(B, Bi, Bj)
        print()
        resultado = efetuar_soma_matrizes(A, B)
        #imprimindo a soma
        sleep(0.5)
        print('\nResultado da soma:')
        imprimir_matriz(resultado, Ai, Aj)
    else:
        print('Não é possível somar: As matrizes devem ser de mesma ordem.')
        sleep(0.5)
        tipo_matriz()
    print()


#chamada principal da subtração de matrizes
def subtrair_matrizes():
    ler_cabecalho('subtrair duas matrizes')
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
        imprimir_matriz(A, Ai, Aj)
        print()
        sleep(0.5)
        print('Matriz B:')
        imprimir_matriz(B, Bi, Bj)
        print()
        resultado = efetuar_subtracao_matrizes(A, B)
        #imprimindo a subtração
        sleep(0.5)
        print('\nResultado da subtração:')
        imprimir_matriz(resultado, Ai, Aj)
    else:
        print('Não é possível subtrair: As matrizes devem ser de mesma ordem.')
        sleep(0.5)
        tipo_matriz()
    print()


#chamada principal da multiplicação de uma matriz por um número real
def multiplicacao_real():
    ler_cabecalho('multiplicação por um número real')
    #definindo a ordem das matrizes 
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    num = ler_num_float('Digite um número que deseja multiplicar: ')
    print()
    #construindo a matriz
    print('Construindo matriz A')
    A = construir_matriz(Ai, Aj)
    print()
    #imprimindo a matriz
    sleep(0.5)
    print('Matriz A:')
    imprimir_matriz(A, Ai, Aj)
    sleep(0.5)
    resultado = efetuar_multi_real(A, num)
    #imprimindo a multiplicação por real
    sleep(0.5)
    print('\nResultado da multiplicação por número real:')
    imprimir_matriz(resultado, Ai, Aj)
    print()


#chamada principal da multiplicação de matrizes
def multiplicacao_matriz():
    ler_cabecalho('multiplicação de matrizes')
    #definindo ordem das matrizes
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    if Aj == Bi:
        #construindo as matrizes
        print('Construindo a matriz A')
        A = construir_matriz(Ai, Aj)
        print()
        print('Construindo a matriz B')
        B = construir_matriz(Bi, Bj)
        print()
        #imprimindo as matrizes
        sleep(0.5)
        print('Matriz A')
        imprimir_matriz(A, Ai, Aj)
        print()
        sleep(0.5)
        print('Matriz B')
        imprimir_matriz(B, Bi, Bj)
        resultado = efetuar_multi_matriz(A, B)
        #imprimindo a multiplicação
        sleep(0.5)
        print('\nResultado da multiplicação de matrizes:')
        imprimir_matriz(resultado, Ai, Bj)
    else:
        print('Não é possível multiplicar as matrizes. O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.')
        sleep(0.5)
        tipo_matriz()
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
    2- Subtrair duas matrizes
    3- Multiplicação de uma matriz por um número real
    4- Multiplicação de matrizes
    ''')
    opcao = ler_escolha('Escolha uma das opções: ')
    print()
    if opcao == 1:
        somar_matrizes()
        sleep(1)
    elif opcao == 2:
        subtrair_matrizes()
    elif opcao == 3:
        multiplicacao_real()
    elif opcao == 4:
        multiplicacao_matriz()
    else:
        pass
