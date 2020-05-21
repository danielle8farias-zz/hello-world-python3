'''
Usuário informa nome de 5 cores. O programa armazena numa lista e retorna em ordem alfabética.
'''

cor1 = input('1ª cor: ')
cor2 = input('2ª cor: ')
cor3 = input('3ª cor: ')
cor4 = input('4ª cor: ')
cor5 = input('5ª cor: ')

#criando a lista
lista_cores = []
#adicionado elementos à lista
lista_cores = [cor1, cor2, cor3, cor4, cor5]
#ordenado a lista
lista_cores.sort()
print(f'As cores são: {lista_cores}')
print()
