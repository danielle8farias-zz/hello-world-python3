#!/usr/bin/env python3.8
'''
Faça um sorteio entre 4 alunos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from random import choice

#programa principal
cabecalho('SORTEIO DE ALUNOS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #upper: joga a string para maiúsculo
    #strip: remove os espaços no começo e no fim
    aluno1 = input('Digite o nome do primeiro aluno: ').strip().upper()
    aluno2 = input('Digite o nome do segundo aluno: ').strip().upper()
    aluno3 = input('Digite o nome do terceiro aluno: ').strip().upper()
    aluno4 = input('Digite o nome do quarto aluno: ').strip().upper()
    lista = [aluno1,aluno2,aluno3,aluno4]
    escolhido = choice(lista)
    print(f'O escolhido foi {escolhido}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
