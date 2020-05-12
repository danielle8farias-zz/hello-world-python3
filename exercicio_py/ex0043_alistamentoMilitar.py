#!/usr/bin/env python3.8

'''
Usuário informa um ano de nascimento e programa verifica se o suário precisa se alistar
e quanto tempo falta.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de data
from datetime import date

#função que verifica se é preciso se alistar
def alistamento(idade):
    #verificando se idade é igual a 18
    if idade == 18:
        #função print retorna uma string na tela
        print('Você tem que se alistar imediatamente!')
    #verificando se idade é menor do que 18
    elif idade < 18:
        #calculando quanto falta para o alistamento
        saldo = 18 - idade
        print('Você ainda não tem 18 anos.')
        #função print retorna uma string formatada na tela
        print(f'Faltam {saldo} anos para seu alistamento.')
    else:
        #calculando quanto passou do alistamento
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos')
    
#programa principal
#chamada da função cabeçalho
cabecalho('ALISTAMENTO MILITAR')
#date.today().year pega o ano do sistema operacional
atual = date.today().year
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável nasc
    nasc = int(input('Seu ano de nascimento: '))
    #calculando idade
    idade = atual - nasc
    print(f'Sua idade é {idade} anos')
    #chamada da função
    alistamento(idade)
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
