'''
Faça um sorteio de apresentação de 4 alunos.
'''
print('-'*50)
print('{: ^50}'.format('SORTEIO DE LISTA DE APRESENTAÇÃO'))
print('-'*50)
from random import shuffle
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
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
