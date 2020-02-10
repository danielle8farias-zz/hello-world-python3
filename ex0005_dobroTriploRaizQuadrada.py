#!/usr/bin/env python3.7
'''
Digite um número e mostro o dobro, o triplo e a raiz quadrada.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o dobro do número informado
def dobro(num):
    dobro = num*2
    return dobro

#função que calcula o triplo do número informado
def triplo(num):
    triplo = num*3
    return triplo

#função que calcula a raiz do número informado
def raiz(num):
    raiz = num**(1/2)
    return raiz

#programa principal
cabecalho('DOBRO, TRIPLO E RAÍZ QUADRADA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = float(input('Digite um número: '))
    dobro_info = dobro(num)
    print(f'O dobro é: {dobro_info}')
    triplo_info = triplo(num)
    print(f'O triplo é: {triplo_info}')
    raiz_info = raiz(num)
    print(f'A raiz quadrada é: {raiz_info}')
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
