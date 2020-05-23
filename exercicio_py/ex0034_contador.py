'''
Usuário informa valores de um contador. Início, fim e o passo.
'''

inicio = int(input('A partir de que número deseja contar? '))
passo = int(input('De quanto em quanto? '))
fim = int(input('Até que valor? '))

for i in range(inicio, fim+1, passo):
    print(i)
