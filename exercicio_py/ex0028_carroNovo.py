#!/usr/bin/env python3.8

'''
Usuário informa a idade de um carro.
Se menor ou igual a 3 anos, o carro é novo, senão o carro é velho.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('carro novo ou antigo?')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    tempo = int(input('Quantos anos tem seu carro? '))
    if tempo <= 3:
        print('Carro novo')
    else:
        print('Carro velho')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
