#!/usr/bin/env python3.7
'''
Leia um número de 0 a 9999 e mostre cada um dos dígitos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('DÍGITOS DE UM NÚMERO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = int(input('Digite um número inteiro: '))
    #separando a unidade
    u = num % 10
    #//10 retirando a unidade %10 separando a dezena(unidade que sobrou)
    d = num // 10 % 10
    #//100 retirando a centena %10 separando a centena(unidade que sobrou)
    c = num // 100 % 10
    #//1000 retirando a unidade de milhar %10 separando a unidade de milhar(unidade que sobrou)
    um = num // 1000 % 10
    #//10000 retirando a dezena de milhar %10 separando a dezena de milhar(unidade que sobrou)
    dm = num // 10000 % 10
    #//100000 retirando a centena de milhar %10 separando a centena de milhar(unidade que sobrou)
    cm = num // 100000 % 10
    #//1000 retirando a unidade de milhão %10 separando a unidade de milhão(unidade que sobrou)
    umi = num // 1000000 % 10
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Unidade de Milhar: {um}')
    print(f'Dezena de Milhar: {dm}')
    print(f'Centena de Milhar: {cm}')
    print(f'Unidade de Milhão: {umi}')
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
