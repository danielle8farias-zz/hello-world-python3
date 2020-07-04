import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_float, ler_divisor, ler_num_int, ler_indice, ler_num_nat


def somar():
    ler_cabecalho('soma')
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    return num1 + num2


def subtrair():
    ler_cabecalho('subtração')
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    return num1 - num2


def multiplicar():
    ler_cabecalho('multiplicação')
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    return num1 * num2


def dividir():
    ler_cabecalho('divisão')
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_divisor('Digite o 2º número: ')
    return num1 / num2


from math import pow
def exponenciar():
    ler_cabecalho('exponenciação')
    base = ler_num_float('Digite o número da base: ')
    expo = ler_num_int('Digite o número do expoente: ')
    return pow(base, expo)


def radiciar():
    ler_cabecalho('radiciação')
    indice = ler_indice('Índice da raiz: ')
    radicando = ler_num_float('Radicando: ')
    if indice % 2 == 0 and radicando >= 0:
        raiz = radicando ** (1/indice)
        return raiz
    elif radicando < 0 and indice % 2 == 1:
        radicando *= -1
        raiz = radicando ** (1/indice)
        return raiz * -1
    else:
        return 'Não é possível calcular a raiz dentro dos Reais.'


def primo():
    ler_cabecalho('número primo')
    n = ler_num_nat("Digite um número inteiro: ")
    i = 0
    c = 0
    while i < n:
        i+= 1
        if (n % i == 0):
            c += 1
    if c == 2:
        print('É PRIMO!')
    else:
        print("não é primo")
    print()

