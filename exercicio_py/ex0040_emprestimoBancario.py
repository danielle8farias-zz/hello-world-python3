#!/usr/bin/env python3.8

'''
Usuário informa o valor de uma casa que deseja comprar, seu salário e em quantos anos deseja pagar.
O programa retorna se empréstimo foi aprovado e o valor da prestação mensal. 
O empréstimo será negado se a prestação exceder 30% do salário.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula a prestação mensal e se o empréstimo foi aprovado
def prestacao(valor_casa, anos, salario):
    #atribuindo a variável prestacao_mensal o resultado da operação
    prestacao_mensal = valor_casa / (anos * 12)
    #:.2f limita o número de duas casas decimais
    #função print retorna uma string formatada na tela
    print(f'O valor da prestação mensal será de R${prestacao_mensal:.2f}')
    #verificando se a prestação é menor do que 30% do salário
    if prestacao_mensal < (salario * 0.3):
        #função print retorna uma string na tela
        print('Empréstimo aprovado!')
    else:
        print('Empréstimo negado.')

#programa principal
#chamada da função cabeçalho
cabecalho('APROVAÇÃO DE EMPRÉSTIMO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável valor_casa
    valor_casa = float(input('Valor da casa que deseja comprar: R$ '))
    salario = float(input('Salário do comprador: R$ '))
    #int() convertendo string para tipo inteiro
    anos = int(input('Em quantos anos pretende pagar? '))
    #chamada da função
    prestacao(valor_casa, anos, salario)
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
