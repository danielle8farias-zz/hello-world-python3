'''
Usuário digita vários valores inteiros. Esses valores são guardados em uma lista. 
Não são permitidos números repetidos.
'''

lista_num = list()

#adicionado números a lista
while True:
    num = int(input('Digite um número: '))
    
    if num not in lista_num:
        lista_num.append(num)
    else:
        print('Esse número já foi adicionado a lista.\n')

    resp = ' '
    while resp not in 'SN':
        resp = input('\nDeseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print(f'\nSua lista: {lista_num}')

lista_num.sort()
print(f'Lista ordenada: {lista_num}')
