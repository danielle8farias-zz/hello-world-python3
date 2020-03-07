#!/usr/bin/env python3.8
'''
Faça um programa que leia um número em radianos e retorne os valores de seno, cosseno e tangente.
'''
#importando parte do código
from mensagem import cabecalho, rodape
from math import radians, sin, cos, tan

#função que calcula o seno
def seno(numero):
    seno = sin(radians(numero))
    return seno

#função que calcula o cosseno
def cosseno(numero):
    cosseno = cos(radians(numero))
    return cosseno

#função que calcula a tangente
def tangente(numero):
    tangente = tan(radians(numero))
    return tangente

#programa principal
cabecalho('SENO COSSENO TANGENTE')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    numero = float(input('Digite um numero: '))
    #:.2f limita o número de duas casas decimais
    print(f'O seno é {seno(numero):.2f}')
    print(f'O cosseno é {cosseno(numero):.2f}')
    print(f'A tangente é {tangente(numero):.2f}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
