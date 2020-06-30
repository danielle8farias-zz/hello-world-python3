#!/usr/bin/env python3.8

'''
Lê o nome de um usuário e retorna o nome com uma mensagem de boas-vindas. Fazendo validação do dado.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta

def ler_nome(msg):
    while True:
        try:
            nome = input(msg).upper().strip()
            #isalpha() se possui apenas letras
            #verificando se nome possui caracteres que não sejam letras
            if not nome.isalpha():
                raise Exception('Digite apenas letras.')
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        #se o 'try' for válido
        else:
            return nome


ler_cabecalho('mensagem de boas-vindas')
while True:
    nome = ler_nome('Qual seu nome? ')
    #verificando se a string não é vazia
    if nome != None:
        print(f'Bem-vinda, {nome}!')
        print()
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    if resposta == 'N':
        break
    else:
        linha()
        print()
rodape()
