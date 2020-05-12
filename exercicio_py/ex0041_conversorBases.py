#!/usr/bin/env python3.8

'''
Usuário informa um número inteiro e escolhe uma opção de conversão desse número.
O programa retorna a conversão escolhida desse número para base binária, octal ou hexadecimal.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que escolhe a opção
def f_escolha(opcao):
    if opcao == 1:
        #[2:] corta as duas primeiras casas        
        #bin() convertendo para binário
        #função print retorna uma string formatada na tela
        print(f'Em binário: {bin(num)[2:]}')
    elif opcao == 2:
        print(f'Em octal: {oct(num)[2:]}')
    elif opcao == 3:
        print(f'Em hexadecimal: {hex(num)[2:]}')
    else:
        #função print retorna uma string na tela
        print('Opção inválida!')

#programa principal
#chamada da função cabeçalho
cabecalho('BASES BINÁRIA, OCTAL E HEXADECIMAL')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num
    num = int(input('Digite um número inteiro: '))
    print('''Escolha a base para conversão:
    [1] binário
    [2] octal
    [3] hexadecimal''')
    opcao = int(input('Sua opção: '))
    #chamada da função
    f_escolha(opcao)
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
