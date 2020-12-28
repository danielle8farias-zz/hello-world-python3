########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função que constrói a matriz.
########

def construir_matriz (num_linhas, num_colunas):
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
    #print() imprime da tela o retorno da função
    print(matriz)
    #retorna a lista 'matriz'
    return matriz


if __name__ == '__main__':
    #chamada da função
    #matriz de ordem 2
    construir_matriz(2,2)
    #matriz de ordem 1x3
    construir_matriz(1,3)
    #matriz de ordem 3x4
    construir_matriz(3,4)

