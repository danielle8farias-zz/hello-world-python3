'''
Faça um programa que leia uma string e retorne as letras embaralhadas.
'''
print('-'*50)
print(f'{"LETRAS EMBARALHADAS":^50}')
print('-'*50)

from random import shuffle

def embaralha(s):
    lista = list(s)
    shuffle(lista)
    nova = ''.join(lista)
    return nova

while True:
    s = input('Digite uma palavra: ').upper().strip()
    print(embaralha(s))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break

print('-'*50)
print(f'{"FIM":^50}')
print('-'*50)