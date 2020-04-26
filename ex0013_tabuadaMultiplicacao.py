#!/usr/bin/env python3.8

'''
Usuário fornece um número inteiro e programa retorna a tabuada de multiplicação desse.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#programa principal
#chamada da função cabeçalho
cabecalho('tabuada de multiplicação')
#função print() retorna uma string na tela
print('Para encerrar digite um número negativo')
#input() recebe como string dado digitado
#int() convertendo string para tipo inteiro
#atribuindo valor a variável num
num = int(input('Digite um número para ver sua tabuada: '))
#laço fazendo o programa rodar até que o usuário decida parar
while num >= 0:
    #retorna linha pontilhada de 40 caracteres
    print('-'*40)
    #laço que vai de 0 a 10
    #não é necessário inicializar a variável i
    for i in range (0,11):
        #atribuindo a variável multiplicação o resultado da operação
        multiplicacao = num * i
        #função print retorna uma string formatada na tela
        #:2 variável i deve ocupar o espaço de dois caracteres
        print(f'{num} * {i:2} = {multiplicacao}')
    #função print vazia não retorna nada; pula uma linha    
    print()
    print('Para encerrar digite um número negativo')
    num = int(input('Digite um número para ver sua tabuada: '))
#chamada da função rodapé
rodape()
