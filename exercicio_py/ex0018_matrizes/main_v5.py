########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Abrindo uma matriz de um arquivo e mostrando seus elementos na tela.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, ler_resposta
from funcoes_matriz import imprimir_matriz, ler_matriz


ler_cabecalho('abrindo matriz de um arquivo')
arquivo = 'matriz4x5.txt'
matriz = ler_matriz(arquivo)
imprimir_matriz(matriz, 4, 5)
criar_rodape()
