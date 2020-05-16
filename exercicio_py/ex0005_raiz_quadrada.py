#!/usr/bin/env python3.8

'''
Usuário informa um número real ou inteiro e programa retorna a raiz quadrada.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulo de raiz quadrada
from math import sqrt
#importando módulos de números
from numeros import ler_num_float

#função que calcula a raiz quadrada
def calcular_raiz_quadrada(num):
    #chamada da função que calcula a raiz quadrada
    #atribuindo retorno da função a variável raiz
    raiz = sqrt(num)
    return raiz


#programa principal
#chamada que lê a função cabeçalho
ler_cabecalho('raiz quadrada')
while True:
    #chamada da função que lê números float
    #atribui a variável 'num' o retorno da função
    num = ler_num_float('Digite um número: ')
    #variável recebe retorno da função
    raiz_quadrada = calcular_raiz_quadrada(num)
    print(f'A raiz de {num} = {raiz_quadrada}')
    # função print() vazia não retorna nada; apenas pula uma linha
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
