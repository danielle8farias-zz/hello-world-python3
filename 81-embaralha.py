'''
Faça um programa que leia uma string e retorne as letras embaralhadas.
'''
from mensagem import cabecalho
from mensagem import rodape
from random import shuffle

cabecalho('LETRAS EMBARALHADAS')

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

rodape()
