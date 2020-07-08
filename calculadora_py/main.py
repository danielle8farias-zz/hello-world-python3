#!/usr/bin/env python3.8

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
from numeros import ler_num_int

#importando pacote de operações aritméticas
from aritmetica.soma_dois_num import somar
from aritmetica.subtrai_dois_num import subtrair
from aritmetica.multiplica_dois_num import multiplicar
from aritmetica.divide_dois_num import dividir
from aritmetica.exponencial import exponenciar
from aritmetica.radicial import radiciar


#from aritmetica import subtrair, multiplicar, dividir, exponenciar, radiciar, primo
from tabuadas import tipo_tabuada
from sequencias import fatorial, pa, fibo
from trigonometria import hipo, razao_trigon
from geometria import verificar_triangulo
from sistema_numeracao import bases
from matrizes import tipo_matriz


from time import sleep


ler_cabecalho('calculadora')
sleep(1)
while True:
    print('''
        0 - sair
        1 - soma
        2 - subtração
        3 - multiplicação
        4 - divisão
        5 - exponenciação
        6 - radiciação
        7 - tabuada
        8 - fatorial
        9 - progressão aritmética (PA)
        10- sequência Fibonacci
        11- lados de um triângulo retângulo
        12- Seno, Cosseno e Tangente
        13- verificar se um número é primo
        14- verifica se é triângulo
        15- conversor de bases
        16- matrizes
    ''')
    opcao = ler_num_int('Escolha uma das opções: ')

    linha()
    sleep(0.5)
    if opcao == 1:
        result = somar()
        print(f'\nSoma: {result}\n')
        sleep(0.5)
    elif opcao == 2:
        result = subtrair()
        print(f'\nSubtração: {result}\n')
        sleep(0.5)
    elif opcao == 3:
        result = multiplicar()
        print(f'\nMultiplicação: {result}\n')
        sleep(0.5)
    elif opcao == 4:
        result = dividir()
        print(f'\nDivisão: {result}\n')
        sleep(0.5)
    elif opcao == 5:
        result = exponenciar()
        print(f'\nExponenciação: {result}\n')
        sleep(0.5)
    elif opcao == 6:
        result = radiciar()
        print(f'\nRadiciação: {result}\n')
        sleep(0.5)
    elif opcao == 7:
        tipo_tabuada()
    elif opcao == 8:
        result = fatorial()
        print(f'\nFatorial: {result}')
    elif opcao == 9:
        pa()
    elif opcao == 10:
        fibo()
    elif opcao == 11:
        hipo()
    elif opcao == 12:
        razao_trigon()
    elif opcao == 13:
        primo()
    elif opcao == 14:
        verificar_triangulo()
    elif opcao == 15:
        bases()
    elif opcao == 16:
        tipo_matriz()
    else:
        break

    sleep(0.5)
    linha()

sleep(0.5)
rodape()
