'''
Leia 5 valores e guarde em uma lista. Retorne o menor e maior valores e suas
respectivas posições.
'''
print('-'*50)
print('{:^50}'.format('MAIOR E MENOR DE UMA LISTA'))
print('-'*50)
valores = []
maior = 0
menor = 0
for v in range(0,5):
    valores.append(int(input(f'Digite o {v+1}º valor: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print()
print('Você digitou os valores: {}'.format(valores))
print('O maior valor é: {} na posição'.format(maior), end=' ')
for i,v in enumerate(valores):
    if v == maior:
        print('{}... '.format(i), end='')
print()
print('O menor valor é: {} na posição'.format(menor), end=' ')
for i,v in enumerate(valores):
    if v == menor:
        print('{}... '.format(i), end='')
print()
print('-'*50)
print('{:^50}'.format('FIM'))
print('-'*50)
