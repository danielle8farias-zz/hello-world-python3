import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float


def calcular_cateto(a, b):
    c = sqrt(a**2 - pow(b, 2))
    return c


#função que verifica a validade da escolha
def ler_escolha(num):
    while True:
        try:
            escolha = int(input(num))
            #verificando se a escolha é diferente de 1 ou 2
            if escolha != 1 and escolha != 2:
                raise Exception('Escolha 1 ou 2.')
        except ValueError:
            print('Digite um número.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return escolha


from math import sqrt, hypot
def hipo():
    ler_cabecalho('lados de um triângulo retângulo')
    print('Digite:')
    print('1 para Hipotenusa')
    print('2 para Cateto')
    print()
    escolha = ler_escolha('O que deseja calcular? ')
    print()
    if escolha == 1:
        b = ler_num_float('Digite o 1º Cateto: ')
        c = ler_num_float('Digite o 2º Cateto: ')
        #a = sqrt(b**2 + c**2)
        a = hypot(b, c)
        print(f'O valor da Hipotenusa é: {a:.2f}')
    else:
        a = ler_num_float('Digite a Hipotenusa: ')
        b = ler_num_float('Digite o Cateto: ')
        c = calcular_cateto(a, b)
        print(f'O valor do outro Cateto é: {c:.2f}')
    print()


from math import radians, sin, cos, tan
def razao_trigon():
    ler_cabecalho('SENO COSSENO TANGENTE')
    numero = ler_num_float('Digite um ângulo: ')
    #radians() convertendo float para radianos
    seno = sin(radians(numero))
    cosseno = cos(radians(numero))
    tangente = tan(radians(numero))
    print(f'O seno é {seno:.2f}')
    print(f'O cosseno é {cosseno:.2f}')
    print(f'A tangente é {tangente:.2f}')
    print()

