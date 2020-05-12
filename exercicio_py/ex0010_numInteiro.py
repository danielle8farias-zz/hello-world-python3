#!/usr/bin/env python3.8

'''
Usuário digita um número com casa decimal e programa retorna o inteiro com arredondamento para cima.
(se a casa decimal for maior do que cinco, vai para o próximo número inteiro)
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#programa principal
#chamada da função cabeçalho
cabecalho('PARTE INTEIRA COM ARREDONDAMENTO PARA CIMA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável num
    num = float(input('Digite um número com casa decimal: '))
    #função print retorna uma string formatada na tela
    #python faz o arredondamento automaticamente
    #:.0f limita o número de casas decimais a zero
    print(f'A parte inteira do número é {num:.0f}')
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
