'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
'''
print('='*25)
print('DEZ TERMOS DE UMA PA')
print('='*25)
A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
An = A1 + (10-1)*r
for n in range(A1, An + r, r):
    print('{}'.format(n), end = '- ')
