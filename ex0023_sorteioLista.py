#!/usr/bin/env python3.8
'''
Faça um sorteio de apresentação de 4 alunos.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/Exercicios-Python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape
from random import shuffle

#programa principal
cabecalho('SORTEIO DE LISTA DE APRESENTAÇÃO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #upper: joga a string para maiúsculo
    #strip: remove os espaços no começo e no fim
    aluno1 = input('Primeiro aluno: ').strip().upper()
    aluno2 = input('Segundo aluno: ').strip().upper()
    aluno3 = input('Terceiro aluno: ').strip().upper()
    aluno4 = input ('Quarto aluno: ').strip().upper()
    lista = [aluno1, aluno2, aluno3, aluno4]
    shuffle(lista)
    print(f'A ordem de apresentação será: {lista}')
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
