#!/usr/bin/env python3.8

'''
Usuário informa um número inteiro e programa retorna a raiz quadrada desse.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de raiz quadrada
from math import sqrt

#função que calcula a raiz quadrada
def raiz_quadrada(num):
    #chamada da função que calcula a raiz quadrada
    #atribuindo retorno da função a variável raiz
    raiz = sqrt(num)
    return raiz

#programa principal
#chamada da função cabeçalho
cabecalho('RAÍZ QUADRADA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num
    num = int(input('digite um número inteiro: '))
    #variável recebe retorno da função
    raiz = raiz_quadrada(num)
    #função print() retorna uma string formatada na tela
    print(f'A raiz de {num} = {raiz}')
    #função print() vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável com espaço para entrar no 2º laço
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
