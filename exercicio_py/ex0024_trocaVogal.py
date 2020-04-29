#!/usr/bin/env python3.8

'''
Usuário digita uma palavra ou frase, e programa retorna a mesma com as vogais trocadas por *(asterísco).
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('TROCA VOGAIS POR ASTERÍSCO')

#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #strip: remove os espaços no começo e no fim
    #lower: transforma a string para minúsculo
    #atribuindo valor a variável palavra
    palavra = input('Escreva uma palavra ou frase: ').strip().lower()
    #inicializando variável antes de entrar no laço
    troca = ''
    #letra é inicializada em 0 por padrão; é o contador
    #len() retorna o tamanho da string
    #percorre de 0 até o tamanho da palavra
    for letra in range(len(palavra)):
        #verifica se em cada posição das letras em palavra possui alguma vogal
        if palavra[letra] in 'aeiou':
            #concatena * a variável troca
            troca += '*'
        else:
            #concatena cada letra de palavra à variável troca
            troca += palavra[letra]
    #função print retorna uma string formatada na tela
    print(f'A nova palavra é: {troca}')
    #função print vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
