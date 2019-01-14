'''
Crie uma lista com vários números. Separe duas listas, a de números pares e a de ímpares.
Exiba as três listas ao final.
'''
print('-'*50)
print('{: ^50}'.format('LISTA DE NºS PARES E ÍMPARES'))
print('-'*50)
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
    print()
print()
print(f'Números pares: {lista_par}')
print(f'Números ímpares: {lista_impar}')
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
