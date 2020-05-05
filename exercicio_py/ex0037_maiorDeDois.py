#!/usr/bin/env python3.8

'''
Usuário informa dois números inteiros e programa retorna o maior número ou se são iguais.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que verifica o maior número
def f_maior(num1,num2):
    #verificando se o 1º número é maior
    if num1 > num2:
        #função print retorna uma string formatada na tela
        print(f'O maior número é: {num1}')
    #verificando se o 2º número é maior        
    elif num2 > num1:
        print(f'O maior número é: {num2}')
    else:
        #função print retorna uma string na tela
        print('Os valores são iguais.')

#programa principal
#chamada da função cabeçalho
cabecalho('MAIOR ENTRE DOIS NÚMEROS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num1
    num1 = int(input("Digite o 1º número inteiro: "))
    num2 = int(input("Digite o 2º número inteiro: "))
    #chamada da função
    f_maior(num1,num2)
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
