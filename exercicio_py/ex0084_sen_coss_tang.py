#!/usr/bin/env python3.8

'''
Usuário fornece um número em radianos e programa retorna os valores de seno, cosseno e tangente.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
from math import radians, sin, cos, tan
from numeros import ler_num_float

#programa principal
ler_cabecalho('SENO COSSENO TANGENTE')
while True:
    numero = ler_num_float('Digite um ângulo: ')
    #radians() convertendo float para radianos
    seno = sin(radians(numero))
    cosseno = cos(radians(numero))
    tangente = tan(radians(numero))
    print(f'O seno é {seno:.2f}')
    print(f'O cosseno é {cosseno:.2f}')
    print(f'A tangente é {tangente:.2f}')
    print()
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    if resposta == 'N':
        break
    else:
        linha()
        print()
rodape()
