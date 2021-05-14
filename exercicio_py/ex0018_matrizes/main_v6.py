########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Multiplicação de uma matriz por um número.
########

#   A é a matriz
#   n é o número
def multiplicar_real(A, n):
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
    #print() imprime da tela o retorno da função
    print(multi_real)
    #retorna a nova matriz com o resultado das multiplicações
    return multi_real


if __name__ == '__main__':
    #chamada da função
    #   matriz = [[1,2],[3,4]]
    #   número real = 5
    multiplicar_real([[1,2],[3,4]], 5) # [[5, 10], [15, 20]]
    multiplicar_real([[1,2],[3,4]], 2.5) # [[2.5, 5.0], [7.5, 10.0]]
