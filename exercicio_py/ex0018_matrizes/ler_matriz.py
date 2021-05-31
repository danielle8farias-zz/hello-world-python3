########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função que lê a matriz de um arquivo.
########

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
        return matriz
