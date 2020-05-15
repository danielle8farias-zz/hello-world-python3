#!/usr/bin/env python3.8

'''
Usuário digita dois números e programa retorna a soma entre eles.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulos de números
from numeros import ler_num_float

#função que realiza a operação soma de dois parâmetros
def somar(n1, n2):
    return n1 + n2


#programa principal
#chamada da função que lê o cabeçalho
ler_cabecalho('somar dois números')
while True:
    #chamada da função que lê números float
    #atribui a variável 'num1' o retorno da função
    num1 = ler_num_float('Digite o 1º número: ')
    num2 = ler_num_float('Digite o 2º número: ')
    soma = somar(num1, num2)
    #print(f'') retorna uma string formatada na tela
    print(f'Soma = {soma}')
    #chamada da função que lê a resposta
    resposta = ler_resposta('Deseja continuar? [S/N] ')
    # função print() vazia não retorna nada; apenas pula uma linha    
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
