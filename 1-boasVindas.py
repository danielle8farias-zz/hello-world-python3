'''
Leia um nome e mostre uma mensagem de boas-vindas
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função
def nome():
    nome = input('Qual o seu nome? ').upper().strip()
    return nome

#programa principal
cabecalho('mensagem de boas vindas')
nome_info = nome()
print(f'Seja bem-vindo {nome_info}!')
rodape()
