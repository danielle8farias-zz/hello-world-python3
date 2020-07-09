import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float

from time import sleep


#função que verifica e identifica o triângulo
def verificar_triangulo():
    ler_cabecalho('VERIFICA SE É TRIÂNGULO')
    lado1 = ler_num_float("Digite o 1º lado do triângulo: ")
    lado2 = ler_num_float("Digite o 2º lado do triângulo: ")
    lado3 = ler_num_float("Digite o 3º lado do triângulo: ")
    print()
    sleep(0.5)
    #verificando se a soma de dois lados quaisquer é maior do que o terceiro lado
    if lado2+lado3 > lado1 and lado1+lado3 > lado2 and lado1+lado2 > lado3:
        #verificando se possui os 3 lados iguais
        if lado1 == lado2 and lado2 == lado3:
            #função print retorna uma string na tela
            print('Triângulo Equilátero: três lados iguais.')
            sleep(0.5)
        #verificando se possui 2 lados iguais
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('Triângulo Isósceles: quaisquer dois lados iguais.')
            sleep(0.5)
        else:
            print('Triângulo Escaleno: três lados diferentes.')
            sleep(0.5)
    else:
        print('Esses valores não formam um triângulo.')
        sleep(0.5)
    print()
