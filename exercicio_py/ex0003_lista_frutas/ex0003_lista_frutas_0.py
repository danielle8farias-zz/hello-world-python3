########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa nome de cinco frutas. O programa armazena numa lista e retorna em ordem alfabética.
########

fruta1 = input('1ª fruta: ')
fruta2 = input('2ª fruta: ')
fruta3 = input('3ª fruta: ')
fruta4 = input('4ª fruta: ')
fruta5 = input('5ª fruta: ')

#criando a lista
lista_frutas = []
#adicionado elementos à lista
lista_frutas = [fruta1, fruta2, fruta3, fruta4, fruta5]
#ordenado a lista
lista_frutas.sort()
print(f'As frutas em ordem alfabética são: {lista_frutas}')
