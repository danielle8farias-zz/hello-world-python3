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

#função que captura um número informado pelo usuário para validação
def ler_num(n):
    #laço
    while True:
        try:
            #input() captura como string o que for digitado
            #float() convertendo a string recebida para tipo flutuante
            #atribuindo valor à variável 'num'
            num = float(input(n))
        #criando exceção
        #   caso o valor digitado seja diferente de um número
        except ValueError as erro:
            #print() retorna uma string na tela
            print('Digite um valor válido!')
            #volta para o início do laço
            continue
        #se o 'try' for válido        
        else:
            #retorna valor de mes
            return num

#função que realiza a operação soma de dois parâmetros
def somar(n1, n2):
    return n1 + n2


#programa principal
#chamada da função que lê o cabeçalho
ler_cabecalho('somar dois números')
while True:
    #chamada da função que lê o número
    #atribui a variável 'num1' o retorno da função
    num1 = ler_num('Digite o 1º número: ')
    num2 = ler_num('Digite o 2º número: ')
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
