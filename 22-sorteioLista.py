'''
Faça um sorteio de apresentação de 4 alunos.
'''
from mensagem import cabecalho
from mensagem import rodape
from random import shuffle

cabecalho('SORTEIO DE LISTA DE APRESENTAÇÃO')

while True:
    aluno1 = input('Primeiro aluno: ')
    aluno2 = input('Segundo aluno: ')
    aluno3 = input('Terceiro aluno: ')
    aluno4 = input ('Quarto aluno: ')
    lista = [aluno1, aluno2, aluno3, aluno4]
    shuffle(lista)
    print('A ordem de apresentação será:')
    print(lista)
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
