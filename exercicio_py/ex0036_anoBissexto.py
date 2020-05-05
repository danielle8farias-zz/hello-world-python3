#!/usr/bin/env python3.8

'''
Usuário informa um ano que deseja verificar e programa retorna se esse é bissexto.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula se o ano é bissexto
def ano_bissexto(ano):
    #verificando se o ano é divisível por 4
    #e se o ano não é divisível por 100
    #ou se o ano é divisível por 400
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        #função print retorna uma string formatada na tela
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} NÃO é bissexto.')

#programa principal
#chamada da função cabeçalho
cabecalho('ANO BISSEXTO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável ano
    ano = int(input('Informe o ano: '))
    #chamada da função
    ano_bissexto(ano)
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
