'''
Usuário informa um número inteiro e programa retorna o seu fatorial; usando o laço for.
'''

num = int(input('Digite um número inteiro: '))
print()
print(f'Calculando {num}!')

i = 0
f = 1
for i in range(num, i, -1):
    if i > 1:
        print(f'{i} x ', end='')
    else:
        print(f'{i} = ', end='')
    f *= i
print(f)
print()
