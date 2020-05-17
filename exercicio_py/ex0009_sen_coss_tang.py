#!/usr/bin/env python3.8

'''
Usuário fornece um número em radianos e programa retorna os valores de seno, cosseno e tangente.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulos de radianos, seno, cosseno e tangente
from math import radians, sin, cos, tan
#importando módulos de números
from numeros import ler_num_float

#programa principal
#chamada que lê a função cabeçalho
ler_cabecalho('SENO COSSENO TANGENTE')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável 'numero'
    numero = ler_num_float('Digite um ângulo: ')
    #radians() convertendo float para radianos
    #atrbuindo a variável o retorno da função
    seno = sin(radians(numero))
    cosseno = cos(radians(numero))
    tangente = tan(radians(numero))
    #:.2f limita o número de duas casas decimais
    #print(f'') retorna uma string formatada na tela
    print(f'O seno é {seno:.2f}')
    print(f'O cosseno é {cosseno:.2f}')
    print(f'A tangente é {tangente:.2f}')
    #função print() vazia não retorna nada; apenas pula uma linha
    print()
    #chamada da função que lê a resposta
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    #verificando se variável 'reposta' é igual a string N
    if resposta == 'N':
        #quebrando o laço
        break
    else:
        #chamada da função linha
        linha()
        print()
#chamada da função rodapé
rodape()
