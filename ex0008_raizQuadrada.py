#!/usr/bin/env python3.8

'''
Usuário informa um número inteiro e programa retorna a raiz quadrada desse.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de raiz quadrada
from math import sqrt

#função que calcula a raiz quadrada
def raiz_quadrada(num):
    raiz = sqrt(num)
    return raiz

#programa principal
cabecalho('RAÍZ QUADRADA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura o que for digitado no teclado
    #int() faz a conversão da string para tipo inteiro
    num = int(input('digite um número inteiro: '))
    #variável recebe retorno da função
    raiz = raiz_quadrada(num)
    print(f'A raiz de {num} = {raiz}')
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
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
