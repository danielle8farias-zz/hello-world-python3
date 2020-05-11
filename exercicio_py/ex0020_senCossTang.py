#!/usr/bin/env python3.8

'''
Usuário fornece um número em radianos e programa retorna os valores de seno, cosseno e tangente.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulos de radianos, seno, cosseno e tangente
from math import radians, sin, cos, tan

#função que calcula o seno
def seno(numero):
    #radians() convertendo float para radianos
    #atrbuindo a variável o retorno da função
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
#chamada da função cabeçalho
cabecalho('SENO COSSENO TANGENTE')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável numero
    numero = float(input('Digite um ângulo: '))
    #:.2f limita o número de duas casas decimais
    #função print retorna uma string formatada na tela
    #chamando função seno()
    print(f'O seno é {seno(numero):.2f}')
    print(f'O cosseno é {cosseno(numero):.2f}')
    print(f'A tangente é {tangente(numero):.2f}')
    #função print vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
