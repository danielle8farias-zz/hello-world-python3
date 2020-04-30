#!/usr/bin/env python3.8

'''
Usuário informa a idade de um carro.
Se menor ou igual a 3 anos, o carro é novo, senão o carro é velho.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('carro novo ou antigo?')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #atribuindo valor a variável tempo
    #int() convertendo string para tipo inteiro    
    tempo = int(input('Quantos anos tem seu carro? '))
    #verificando se o tempo é menor ou igual a 3
    if tempo <= 3:
        #função print retorna uma string na tela
        print('Carro novo')
    else:
        print('Carro velho')
    #função print vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável vazia para entrar no 2º laço    
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
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
