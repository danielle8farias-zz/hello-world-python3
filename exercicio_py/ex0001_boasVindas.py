#!/usr/bin/env python3.8

'''
Lê o nome de um usuário e retorna o nome com uma mensagem de boas-vindas.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#programa principal
#chamada da função cabeçalho
cabecalho('mensagem de boas vindas')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #upper: joga a string para maiúsculo
    #strip: remove os espaços no começo e no fim
    #atribuindo valor a variável nome
    nome = input('Qual o seu nome? ').upper().strip()
    #função print() retorna uma string formatada na tela
    print(f'Seja bem-vindo {nome}!')
    # função print() vazia não retorna nada; apenas pula uma linha
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N]? ').upper().strip()[0]
    #verificando se variável reposta é igual a string N        
    if resposta == 'N':
        #quebrando o 1º laço
        break
    print()
#chamada da função rodapé    
rodape()
