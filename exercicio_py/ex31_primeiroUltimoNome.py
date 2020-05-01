#!/usr/bin/env python3.8

'''
Usuário informa nome completo e programa retorne apenas o primeiro e o último nome.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('Retornando o primeiro e último nome')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #atribuindo valor a variável nome
    #strip() remove os espaços no começo e no fim
    nome = input('Digite seu nome completo: ').strip()
    #split() transforma a string em lista, separando pelos espaços digitados
    n = nome.split()
    #função print retorna uma string formatada na tela
    #[0] pegando o primeiro item da lista
    print(f'Seu primeiro nome é: {n[0]}')
    #[-1] pegando o último item da lista
    print(f'Seu último nome é: {n[-1]}')
    #função print vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
