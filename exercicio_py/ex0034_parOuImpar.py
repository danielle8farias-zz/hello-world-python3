#!/usr/bin/env python3.8

'''
Usuário informa um número inteiro e programa retorna se esse número é ímpar ou par.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula se o número é par ou ímpar
def par_impar(num):
    #verifica se a divisão por 2 tem resto 1
    if num % 2 == 1:
        #função print retorna uma string formatada na tela
        print(f'O número {num} é ímpar.')
    else:
        print(f'O número {num} é par.')

#programa principal
#chamada da função cabeçalho
cabecalho('VERIFICA SE É PAR OU ÍMPAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num
    num = int(input("Digite um número: "))
    #chamada da função
    par_impar(num)
    #função print vazia não retorna nada; pula uma linha    
    print()
    #inicializa a variável com espaço para entrar no 2º laço
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
