'''
Leia um nome e mostre uma mensagem de boas-vindas
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

cabecalho('mensagem de boas vindas')

def nome():
    nome = input('Qual o seu nome? ').upper().strip()
    print(f'Seja bem-vindo {nome}!')

nome()

rodape()
