#!/usr/bin/env python3.8

'''
Usuário fornece um número real (do conjunto dos reais) e o programa retorna a parte inteira sem arredondamento.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de arredondamento para baixo
from math import trunc

#programa principal
#chamada da função cabeçalho
cabecalho('PARTE INTEIRA DE UM NÚMERO REAL')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável num
    num = float(input('Digite um número real: '))
    #trunc() arredondando valor para baixo, caso seja necessário
    #função print retorna uma string formatada na tela
    print(f'A parte inteira do valor digitado foi {trunc(num)}.')
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
