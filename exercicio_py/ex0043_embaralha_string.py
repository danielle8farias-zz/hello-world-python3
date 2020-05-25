'''
Usuário informa uma string e computador retorna as letras embaralhadas.
'''

from random import shuffle

msg = input('Digite uma palavra ou frase: ').upper().strip()

#usa-se list() ao invés de [] para que seja criado uma lista
#   com cada caractere da string
lista = list(msg)
#embaralhando os elementos da lista
shuffle(lista)
#unindo os elementos da lista em uma string
nova_msg = ''.join(lista)
print(nova_msg)
