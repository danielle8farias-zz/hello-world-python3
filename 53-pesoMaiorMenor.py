'''
Leia o peso de 5 pessoas. Mostre o maior e o menor peso lido.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('INFORMANDO O MAIOR E O MENOR PESO')

maior = 0
menor = 0
for n in range(1,6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso é {}Kg.'.format(maior))
print('O menor peso é {}Kg.'.format(menor))

rodape()
