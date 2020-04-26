#!/usr/bin/env python3.8

'''
Programa retorna na tela dois números aleatórios.
O primeiro, entre 0 e 1. O segundo, entre 1 e 10.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de números aleatórios
from random import randint, random

#função que chama as outras duas funções de números aleatórios
def num_aleatorio():
    #função que retorna um número aleatório entre [0 e 1)
    #zero fechado (inclui o zero) e um aberto (não inclui o um)
    #atribuindo a variável num1 o retorno da função
    num1 = random()
    #função que retorna um número aleatório entre 1 e 10
    num2 = randint(1,10)
    # dois retornos
    return num1, num2

#programa principal
#chamada da função cabeçalho
cabecalho('NÚMEROS ALEATÓRIOS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    # duas variáveis recebem os retornos da função e fazem a chamada dessa função
    num1, num2 = num_aleatorio()
    #função print retorna uma string formatada na tela
    print(f'Primeiro número aleatório entre 0 e 1: {num1}')
    print(f'Segundo número aleatório entre 1 e 10: {num2}')
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
