#!/usr/bin/env python3.8

'''
Usuário informa um número e programa retorna o anterior e sucessor desse.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que retorna o número antecessor e sucessor
def ant_suc(num):
    #atribuindo resultado da subtração a variável ant
    ant = num - 1
    suc = num + 1
    #retornando dois valores
    return ant, suc

#programa principal
cabecalho('NÚMERO ANTERIOR E SUCESSOR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num
    num = int(input('Escreva um número: '))
    # duas variáveis recebendo o retorno duplo da função
    ant, suc = ant_suc(num)
    # função print() vazia não retorna nada; apenas pula uma linha
    print()
    #função print() retorna uma string formatada na tela
    print(f'O antecessor é {ant} e o sucessor {suc}.')
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
rodape()
