#!/usr/bin/env python3.8

'''
Usuário digita um número natural inteiro e programa verifica se esse é número primo.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('verifica se é primo')

#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #int() convertendo string para tipo inteiro
    #input() recebe como string dado digitado
    #atribuindo valor a variável n
    n = int(input("Digite um número inteiro: "))
    #inicializando primeira variável contadora
    i = 0
    #inicializando segunda variável contadora
    c = 0
    #enquanto o contador i for menor do que n
    while i < n:
        #incrementando contador em +1
        i+= 1
        #verificando se o resto da divisão de n por i é igual a zero
        if (n % i == 0):
            #incrementando contador c em +1
            #esse contador serve para guardar quantos divisores o num possui
            c += 1
    #verificando se o c é igual a 2
    #isso indica que o número dado possui exatamente dois divisores; o que o classifica como primo            
    if c == 2:
        print('É PRIMO!')
    else:
        print("não é primo")
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
