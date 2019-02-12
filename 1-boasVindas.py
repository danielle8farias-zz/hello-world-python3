'''
Leia um nome e mostre uma mensagem de boas-vindas
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('mensagem de boas vindas')

nome = input('Qual o seu nome? ').upper().strip()
print()
print('Seja bem-vinda(o), {}!'.format(nome))

rodape()
