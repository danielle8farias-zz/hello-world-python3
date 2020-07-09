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
from aritmetica.primo import primo

#importando pacote de tabuadas
from tabuadas.main_tabuada import tipo_tabuada

#importando pacotes de sequências
from sequencias.fatorial import fatorial
from sequencias.progressao_aritmetica import pa
from sequencias.fibonacci import fibo

#importando pacotes de geometria
from geometria.triangulo import verificar_triangulo

#importando pacotes de trigonometria
from trigonometria.hipotenusa import hipo
from trigonometria.razao_trigonometrica import razao_trigon

#importando pacotes de sistemas numéricos
from sistema_numeracao.mudanca_base import bases


from matrizes import tipo_matriz


from time import sleep


ler_cabecalho('calculadora')
sleep(1)
while True:
    print('''
    0 - sair            6 - radiciação                         12- Seno, Cosseno e Tangente
    1 - soma            7 - tabuada                            13- verificar se um número é primo
    2 - subtração       8 - fatorial                           14- verifica se é triângulo
    3 - multiplicação   9 - progressão aritmética (PA)         15- conversor de bases
    4 - divisão         10- sequência Fibonacci
    5 - exponenciação   11- lados de um triângulo retângulo
        
                
        
        16- matrizes
    ''')
    opcao = ler_num_int('Escolha uma das opções: ')

    linha()
    sleep(0.5)
    #soma
    if opcao == 1:
        result = somar()
        print(f'\nSoma: {result}\n')
        sleep(0.5)
    
    #subtração
    elif opcao == 2:
        result = subtrair()
        print(f'\nSubtração: {result}\n')
        sleep(0.5)
    
    #multiplicação
    elif opcao == 3:
        result = multiplicar()
        print(f'\nMultiplicação: {result}\n')
        sleep(0.5)

    #divisão
    elif opcao == 4:
        result = dividir()
        print(f'\nDivisão: {result}\n')
        sleep(0.5)

    #potência
    elif opcao == 5:
        result = exponenciar()
        print(f'\nExponenciação: {result}\n')
        sleep(0.5)

    #raiz
    elif opcao == 6:
        result = radiciar()
        print(f'\nRadiciação: {result}\n')
        sleep(0.5)

    #tabuadas
    elif opcao == 7:
        tipo_tabuada()
        sleep(0.5)

    #fatorial
    elif opcao == 8:
        result = fatorial()
        print(f'\nFatorial: {result}\n')
        sleep(0.5)

    #progressão aritmética
    elif opcao == 9:
        pa()
        sleep(0.5)

    #fibonacci
    elif opcao == 10:
        fibo()
        sleep(0.5)

    #hipotenusa e catetos
    elif opcao == 11:
        hipo()
        sleep(0.5)
    
    #seno, cosseno, tangente
    elif opcao == 12:
        razao_trigon()
        sleep(0.5)
    
    #ver se é primo
    elif opcao == 13:
        primo()
        sleep(0.5)

    #verifica se lados formam um triângulo
    elif opcao == 14:
        verificar_triangulo()
        sleep(0.5)

    #conversor de bases
    elif opcao == 15:
        bases()
        sleep(0.5)

    elif opcao == 16:
        tipo_matriz()
    else:
        break

    sleep(0.5)
    linha()

sleep(0.5)
rodape()
