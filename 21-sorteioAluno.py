'''
Faça um sorteio entre 4 alunos.
'''
print('-'*50)
print('{: ^50}'.format('SORTEIO DE ALUNOS'))
print('-'*50)
from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))
