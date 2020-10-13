########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa nome de cinco frutas. O programa armazena numa lista e retorna em ordem alfabética.
########

lista_frutas = []
for i in range(1,6):
    fruta = input(f'{i}ª fruta: ')
    #append() adiciona ao final a lista um item
    lista_frutas.append(fruta)
lista_frutas.sort()
print(f'As frutas em ordem alfabética são: {lista_frutas}')
