########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o comprimento de 3 retas e programa retorna se é possível formar um triângulo e que tipo de triângulo.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_float


#função que verifica e identifica o triângulo
def verificar_triangulo(lado1, lado2, lado3):
    #verificando se a soma de dois lados quaisquer é maior do que o terceiro lado
    if lado2+lado3 > lado1 and lado1+lado3 > lado2 and lado1+lado2 > lado3:
        #verificando se possui os 3 lados iguais
        if lado1 == lado2 and lado2 == lado3:
            #função print retorna uma string na tela
            print('Triângulo Equilátero: três lados iguais.')
        #verificando se possui 2 lados iguais
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('Triângulo Isósceles: quaisquer dois lados iguais.')
        else:
            print('Triângulo Escaleno: três lados diferentes.')
    else:
        print('Esses valores não formam um triângulo.')


#programa principal
ler_cabecalho('VERIFICA SE É TRIÂNGULO')
while True:
    lado1 = ler_num_float("Digite o 1º lado do triângulo: ")
    lado2 = ler_num_float("Digite o 2º lado do triângulo: ")
    lado3 = ler_num_float("Digite o 3º lado do triângulo: ")
    verificar_triangulo(lado1, lado2, lado3)
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('\nDeseja continuar? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()
