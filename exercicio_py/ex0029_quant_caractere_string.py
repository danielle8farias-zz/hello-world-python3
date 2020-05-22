'''
Usuário informa um nome completo (nome e sobrenome) e 
programa retorna quantos letras o nome completo possui (excluindo os espaços) e 
quantas letras o primeiro nome possui.
'''

nome_completo = input('Digite seu nome completo: ')

#count(' ') conta os espaços em branco
#len() retorna o tamanho da string
tamanho_completo = len(nome_completo) - nome_completo.count(' ')
print(f'Seu nome completo possui: {tamanho_completo} letras.')
#find() retorna a posição de um caractere
#   nesse caso queremos enccontrar o primeiro espaço
posicao_nome = nome_completo.find(' ')
print(f'Seu primeiro nome possui: {posicao_nome} letras.')
print()
