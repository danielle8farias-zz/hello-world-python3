'''
Informe um ângulo e calcule o valor do seno, cosseno e tangente.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from math import radians
from math import sin
from math import cos
from math import tan

#função que calcula o seno
def seno(angulo):
    seno = sin(radians(angulo))
    return seno

#função que calcula o cosseno
def cosseno(angulo):
    cosseno = cos(radians(angulo))
    return cosseno

#função que calcula a tangente
def tangente(angulo):
    tangente = tan(radians(angulo))
    return tangente

#programa principal
cabecalho('SENO COSSENO TANGENTE')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    angulo = float(input('Digite um ângulo: '))
    #:.2f limita o número de duas casas decimais
    print(f'O seno é {seno(angulo):.2f}')
    print(f'O cosseno é {cosseno(angulo):.2f}')
    print(f'A tangente é {tangente(angulo):.2f}')
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
