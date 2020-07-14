'''
Usuário digita uma lista de valores inteiros. A lista pára de ser preenchida no momento de escolha do usuário. O programa retorna essa lista ordenada. Sem usar o método sort.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_int


lista_A = []

while True:
    num = ler_num_int('Digite o valor que deseja adicionar na lista: ')
    lista_A.append(num)
    resposta = ' '
    print()
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    if resposta == 'N':
        break
    print()

print(f'Sua lista: {lista_A}')


#ordenando a lista
aux = lista_A[:]
lista_ordenada = list()

while len(lista_ordenada) != len(lista_A):
    menor = aux[0]
    for item in aux:
        if item < menor:
            menor = item
    lista_ordenada.append(menor)
    aux.remove(menor)

print(f'\nLista ordenada: {lista_ordenada}')
rodape()
