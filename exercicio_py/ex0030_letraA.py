#!/usr/bin/env python3.8

'''
Usuário informa uma string e programa verifica o número de vezes que a letra A aparece
e qual a posição da primeira letra e última letras A.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('verificando letra a')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #atribuindo valor a variável frase
    #lower: joga a string para minúsculo
    #strip: remove os espaços no começo e no fim
    frase = input('Digite uma frase: ').lower().strip()
    #função print retorna uma string formatada na tela
    #count() conta o número de vezes que aparece a letra indicada
    print(f'A letra A aparece {frase.count("a")} vezes.')
    #find() indica a posição do caractere
    print(f'A primeira letra A está na posição {frase.find("a")}')
    #rfind() indica a posição do caractere começando pelo final da string
    print(f'A última letra A está na posição {frase.rfind("a")}')
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
