'''
Leia um nome e mostre uma mensagem de boas-vindas
'''
nome = input('Qual o seu nome? ').upper().strip()
print('='*50)
print('Seja bem-vinda(o), {}!'.format(nome))
