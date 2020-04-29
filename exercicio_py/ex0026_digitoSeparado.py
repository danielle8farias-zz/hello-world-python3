#!/usr/bin/env python3.8

'''
Usuário informa um número inteiro entre 0 e 9999 e programa 
retorna a posição decimal de cada algarismo;
unidade, dezena, centena, etc.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que separa as casas decimais
def digitos(num):
    #separando a unidade
    #atribuindo a variável o resultado da operação
    u = num % 10
    #função print retorna uma string formatada na tela
    print(f'Unidade: {u}')
    #//10 retirando a unidade; %10 separando a dezena(unidade que sobrou)
    d = num // 10 % 10
    print(f'Dezena: {d}')
    #//100 retirando a centena; %10 separando a centena(unidade que sobrou)
    c = num // 100 % 10
    print(f'Centena: {c}')
    #//1000 retirando a unidade de milhar; %10 separando a unidade de milhar(unidade que sobrou)
    um = num // 1000
    print(f'Unidade de Milhar: {um}')

#programa principal
#chamada da função cabeçalho
cabecalho('posição decimal')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #2º laço; enquanto o usuário escolher número fora do escopo
    while True:
        #função print retorna uma string na tela
        print('Escolha um número inteiro entre 0 e 9999')
        #input() recebe como string dado digitado
        #int() convertendo string para tipo inteiro    
        num = int(input('Digite um número: '))
        #verificando se número está entre 0 e 9999
        if num >= 0 and num < 10000:
            #quebrando 2º laço
            break
        else:
            print('Número inválido!')
            #função print vazia não retorna nada; pula uma linha
            print()
    #chamada da função
    digitos(num)
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
