#!/usr/bin/env python3.8

'''
Usuário informa quantos alunos deseja cadastrar;
o programa cria uma lista com a quantidade de alunos,
em seguida pede o nome para cada um deles e por fim, 
retorna o nome de um aluno de maneria aleatória.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo que escolhe um elemento aleatório de uma lista
from random import choice
#importando função que suspende em segundos a execução do programa
from time import  sleep

#programa principal
#chamada da função cabeçalho
cabecalho('SORTEIO DE ALUNOS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num_alunos
    #input() recebe como string dado digitado
    num_alunos = int(input('Quantos alunos deseja cadastrar? '))
    #inicializando a variável contadora
    i = 1
    #criando lista
    lista_alunos = []
    #range vai até um valor a menos do parâmetro, por isso +1
    #laço que começa em 1 e vai até num_alunos
    for i in range(i, num_alunos+1):
        #i assume valores de 1 a num_alunos; conforme a execução do laço
        #atribuindo a variável os nomes dos alunos
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        aluno = input(f'Digite o {i}º aluno: ').strip().upper()
        #adicionando os alunos a lista(vetor)
        lista_alunos.append(aluno)
    #função print vazia não retorna nada; pula uma linha
    print()
    #função print retorna uma string na tela
    print('Os alunos registrados foram:')
    print(lista_alunos)
    #parando a execução por 1.5 segundos
    sleep(1.5)
    #escolhendo um aluno aleatório da lista
    escolhido = choice(lista_alunos)
    #função print retorna uma string formatada na tela
    print(f'O escolhido foi: {escolhido}')
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
