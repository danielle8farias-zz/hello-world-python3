#!/usr/bin/env python3.8

'''
Usuário fornece um número inteiro e programa retorna a tabuada de multiplicação desse.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulos de números
from numeros import ler_num_int

#programa principal
#chamada função que lê o cabeçalho
ler_cabecalho('tabuada de multiplicação')
while True:
    #atribui a variável 'num' o retorno da função
    num = ler_num_int('Digite um número inteiro: ')
    # função print() vazia não retorna nada; apenas pula uma linha
    print()
    #laço que vai de 0 a 10
    #não é necessário inicializar a variável i
    for i in range (0,11):
        #atribuindo a variável 'multiplicação' o resultado da operação
        multiplicacao = num * i
        #função print retorna uma string formatada na tela
        #:2 variável i deve ocupar o espaço de dois caracteres
        print(f'{num} x {i:2} = {multiplicacao}')
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
