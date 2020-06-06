#!/usr/bin/env python3.8

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
from time import sleep
from aritmetica import somar, subtrair, multiplicar, dividir, exponenciar, radiciar
from tabuadas import tipo_tabuada
from numeros import ler_num_int


ler_cabecalho('calculadora')
sleep(1)
while True:
    print('''
        0- sair
        1- soma
        2- subtração
        3- multiplicação
        4- divisão
        5- exponenciação
        6- radiciação
        7- tabuada
    ''')
    opcao = ler_num_int('Escolha uma das opções: ')

    linha()
    sleep(0.5)
    if opcao == 1:
        result = somar()
        print(f'\nSoma: {result}')
    elif opcao == 2:
        result = subtrair()
        print(f'\nSubtração: {result}')
    elif opcao == 3:
        result = multiplicar()
        print(f'\nMultiplicação: {result}')
    elif opcao == 4:
        result = dividir()
        print(f'\nDivisão: {result}')
    elif opcao == 5:
        result = exponenciar()
        print(f'\nExponenciação: {result}')
    elif opcao == 6:
        result = radiciar()
        print(f'\nRadiciação: {result}')
    elif opcao == 7:
        tipo_tabuada()
    else:
        break

    sleep(0.5)
    linha()

sleep(0.5)
rodape()
