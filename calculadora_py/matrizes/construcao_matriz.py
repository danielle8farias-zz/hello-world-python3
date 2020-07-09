import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from numeros import ler_num_float


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
