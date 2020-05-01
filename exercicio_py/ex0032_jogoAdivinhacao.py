#!/usr/bin/env python3.8

'''
Faça um jogo de adivinhação de números, entre os números 0 a 5.
Usuário digita um número, computador escolhe um número e se os números forem
os mesmos, usuário ganha.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape, linha
#importando módulo para número aleatório
from random import randint
#importando função que suspende em segundos a execução do programa
from time import sleep

#chamada da função cabeçalho
cabecalho('jogo adivinhação')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #atribuindo a variável computador o retorno da função
    #randint(0,5) número aleatório entre 0 e 5
    computador = randint(0, 5)
    #chamada da função linha
    linha()
    #função print retorna uma string na tela
    print('Por favor escolha um número de 0 a 5')
    linha()
    #int() convertendo string para tipo inteiro
    #input() recebe como string dado digitado
    #atribuindo valor a variável jogador
    jogador = int(input('Em que número eu pensei? '))
    print('Processando...')
    #parando a execução por 1.5 segundos
    sleep(1.5)
    #verificando se valor de jogador é igual ao de computador
    if jogador == computador:
        print('PARABÉNS! Você conseguiu adivinhar!')
    else:
        #função print retorna uma string formatada na tela
        print(f'Eu pensei no número {computador}.')
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
