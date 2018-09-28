'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
'''
print('='*25)
print('DEZ TERMOS DE UMA PA')
print('='*25)
A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
An = A1
while cont <= 10:
    print('{}'.format(An), end=' ')
    print(' - ' if cont < 10 else ' ', end=' ')
    An = An + r
    cont += 1
