#!/usr/bin/env python3.8

'''
Lê o nome de um usuário e retorna o nome com uma mensagem de boas-vindas.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta

#definindo função que lê o nome
def ler_nome(msg):
    #laço
    while True:
        try:
            #strip: remove os espaços no começo e no fim
            #upper() transforma string em maiúscula
            #input() captura como string o que for digitado
            #atribuindo valor à variável 'nome'
            nome = input(msg).upper().strip()
            #isalpha() se possui apenas letras
            #verificando se nome possui caracteres que não sejam letras
            if not nome.isalpha():
                #criando exceção
                raise Exception('Digite apenas letras.')
        #chama a exceção criada
        #variável 'erro' retorna a mensagem da exceção
        except Exception as erro:
            #print(f'') retorna uma string formatada na tela
            print(f'Valor inválido: {erro}')
            #volta para o início do laço
            continue
        #se o 'try' for válido
        else:
            #retorna valor de nome
            return nome


#programa principal
#chamada da função que lê o cabeçalho
ler_cabecalho('mensagem de boas-vindas')
while True:
    #chamada da função que lê o nome
    #atribui a variável 'nome' o retorno da função
    nome = ler_nome('Qual seu nome? ')
    #verificando se a string não é vazia
    if nome != None:
        print(f'Bem-vinda, {nome}!')
    #chamada da função que lê a resposta
    resposta = ler_resposta('Deseja continuar? [S/N]')
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
