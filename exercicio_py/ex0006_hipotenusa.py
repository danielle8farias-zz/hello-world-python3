#!/usr/bin/env python3.8

'''
Usuário escolhe o que deseja calcular entre cateto ou hipotenusa e programa retorna o valor escolhido.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulo de raiz quadrada
from math import sqrt, hypot
#importando módulos de números
from numeros import ler_num_float

#função que calcula a hipotenusa
def calcular_cateto(a, b):
    #chamada da função sqrt que calcula a raiz quadrada
    #   **2 elevado ao quadrado 
    #   ou pow(base, potência)
    c = sqrt(a**2 - pow(b, 2))
    #retorno da função    
    return c


#função que verifica a validade da escolha
def ler_escolha(num):
    #laço
    while True:
        try:
            #input() captura como string o que for digitado
            #int() convertendo a string recebida para tipo inteiro
            #atribuindo valor à variável 'escolha'
            escolha = int(input(num))
            #verificando se a escolha é diferente de 1 ou 2
            if escolha != 1 and escolha != 2:
                #criando exceção
                raise Exception('Escolha 1 ou 2.')
        #caso seja digitado espaços ou ENTER
        #variável 'erro' retorna a mensagem da exceção
        except ValueError as erro:
            #print() retorna uma string na tela
            print('Digite um número.')
            #volta para o início do laço
            continue
        #chama a exceção criada
        except Exception as erro1:
            #print(f'') retorna uma string formatada na tela
            print(f'Valor inválido: {erro1}')
            continue
        #se o 'try' for válido        
        else:
            return escolha


#programa principal
#chamada que lê a função cabeçalho
ler_cabecalho('hipotenusa')
while True:
    print('Digite:')
    print('1 para Hipotenusa')
    print('2 para Cateto')
    #função print() vazia não retorna nada; apenas pula uma linha
    print()
    #validar resposta
    #atribui a variável 'escolha' o retorno da função
    escolha = ler_escolha('O que deseja calcular? ')
    print()
    if escolha == 1:
        b = ler_num_float('Digite o 1º Cateto: ')
        c = ler_num_float('Digite o 2º Cateto: ')
        #a = sqrt(b**2 + c**2)
        a = hypot(b, c)
        print(f'O valor da Hipotenusa é: {a:.2f}')
    else:
        a = ler_num_float('Digite a Hipotenusa: ')
        b = ler_num_float('Digite o Cateto: ')
        c = calcular_cateto(a, b)
        print(f'O valor do outro Cateto é: {c:.2f}')
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
