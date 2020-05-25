'''
Usuário informa o 1º termo de uma PA e sua razão. 
O programa retorna os 10 primeiros termos dessa PA. Usando for.
'''

A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))

#fóruma da Progressão aritmética
#   calculando o último termo
An = A1 + (10-1)*r
#laço que vai de A1 até An+r de r em r
for n in range(A1, An + r, r):
    print(f'{n}', end = ' -> ')
print('FIM')
