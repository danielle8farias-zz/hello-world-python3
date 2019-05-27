'''
Leia um nome e mostre uma mensagem de boas-vindas
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#chamando a importação
cabecalho('mensagem de boas vindas')

#função
def nome():
    nome = input('Qual o seu nome? ').upper().strip()
    print(f'Seja bem-vindo {nome}!')

#programa principal
nome()

#chamando a importação
rodape()
