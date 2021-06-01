########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Diversas funções para matrizes.
########

def construir_matriz (num_linhas, num_colunas):
    '''
    Recebe um número de linhas e colunas e contrói uma matriz com os
    valores escolhidos pelo usuário
    '''
    print(f'Matriz com {num_linhas} linhas e {num_colunas} colunas.\n')
    #criando lista vazia
    matriz = []
    #laço for
    #   para cada item até o número de listas dado pelo usuário
    #   num_linhas -1 pois o range começa em zero
    #   percorrendo as linhas da matriz
    for i in range(num_linhas):
        linha = []
        #percorrendo as colunas da matriz
        for j in range(num_colunas):
            #variável 'valor' recebe o que foi digitado
            #float() converte para número real
            #input() capitura o que foi digitado no teclado
            valor = float(input(f'Digite o valor A{i}{j}: '))
            #adiciona ao final da lista 'linha' o valor
            linha.append(valor)
        #adiciona ao final da lista 'matriz', a lista 'linha'
        #   lista dentro de outra lista; lista composta
        matriz.append(linha)
    #retorna a lista 'matriz'
    return matriz


def somar_matrizes (A, B):
    '''
    Recebe duas matrizes e retorna a soma entre elas
    '''
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


def multiplicar_matrizes (A, B):
    '''
    Recebe duas matrizes e retorna a multiplicação entre elas.
    '''
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    multiplicacao = []
    for i in range(num_linhas_A):
        linha = []
        for j in range(num_colunas_B):
            soma = 0
            for k in range(num_colunas_A):
                soma += A[i][k] * B[k][j]
            linha.append(soma)
        multiplicacao.append(linha)
    return multiplicacao


from time import sleep

def imprimir_matriz(M, Mi, Mj):
    '''
    Recebe a matriz, o número de linhas e colunas e retorna ao usuário
    a matriz de modo mais legível
    '''
    for i in range(Mi):
        for j in range(Mj):
            sleep(0.5)
            print(f'[{M[i][j]:^5}]', end='', flush=True)
        print()


def ler_matriz(nome):
    '''
    Abre um arquivo com uma matriz e guarda os dados numa lista.
    '''
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
        return matriz


def multiplicar_real(A, n):
    '''
    Recebe uma matriz e um número e retorna a multiplicação
    dessa matriz por esse número.
    '''
    #len() pega o tamanho da lista (matriz) A
    #   número de linhas é o comprimento da matriz
    num_linhas = len(A)
    #número de colunas é o tamanho de uma das sublistas de matriz
    num_colunas = len(A[0])
    #criando lista vazia que armazenará o resultado da multiplicação
    multi_real = []
    #laço for
    #   para cada item até o número de linhas da matriz
    #   range() vai de zero até (num_linhas -1)
    #   percorrendo as linhas da matriz
    for i in range(num_linhas):
        #criando a lista para as linhas
        linha = []
        #percorrendo as colunas da matriz
        for j in range(num_colunas):
            #multiplicando cada item da matriz pelo número real
            valor = (n * A[i][j])
            #adiciona o resultado da multiplicação ao final da lista linha
            linha.append(valor)
        #adiciona cada uma das linhas a matriz que guardará o resultado
        multi_real.append(linha)
    #retorna a nova matriz com o resultado das multiplicações
    return multi_real


def matriz_nula(Ai, Aj):
    N = []
    for i in range(Ai):
        # criando as colunas dentro de cada linha
        linha = [0] * Aj
        N.append(linha)
    return N


def matriz_transposta(M):
    n_linhas = len(M)
    n_colunas = len(M[0])
    T = matriz_nula (n_colunas, n_linhas)
    for i in range(n_linhas):
        for j in range(n_colunas):
            # invertendo as posições pois é propriedade da matriz transposta
            T[j][i]= M[i][j]
    return T
