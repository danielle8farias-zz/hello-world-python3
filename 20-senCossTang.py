'''
Informe um ângulo e calcule o valor do seno, cosseno e tangente.
'''
from mensagem import cabecalho
from mensagem import rodape
from math import radians

cabecalho('SENO COSSENO TANGENTE')

def seno(angulo):
    from math import sin
    seno = sin(radians(angulo))
    return seno


def cosseno(angulo):
    from math import cos
    cosseno = cos(radians(angulo))
    return cosseno


def tangente(angulo):
    from math import tan
    tangente = tan(radians(angulo))
    return tangente
    
    
while True:
    angulo = float(input('Digite um ângulo: '))
    print('O seno é {:.2f}'.format(seno(angulo)))
    print('O cosseno é {:.2f}'.format(cosseno(angulo)))
    print('A tangente é {:.2f}'.format(tangente(angulo)))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
