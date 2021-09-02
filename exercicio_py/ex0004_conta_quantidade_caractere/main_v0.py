########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa nome e sobrenome. 
# O programa retorna quantas letras o nome completo possui (excluindo espaços) 
# e quantas letras o primeiro nome possui. 
########

nome_completo = input('Digite seu nome completo: ')

#count(' ') conta os espaços em branco
#len() retorna o tamanho da string
#   retirando espaço entre os nomes
tamanho_completo = len(nome_completo) - nome_completo.count(' ')
print(f'Seu nome completo possui: {tamanho_completo} letras.')
#find() retorna a posição de um caractere
#   nesse caso queremos encontrar o primeiro espaço
num = nome_completo.find(' ')
print(f'Seu primeiro nome possui: {num} letras.\n')
