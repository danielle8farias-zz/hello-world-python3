'''
Usuário informa um número inteiro e programa retorna o seu fatorial; usando o laço while.
'''

num = int(input('Digite um número inteiro: '))
print()
print(f'Calculando {num}!')
i = num
f = 1
while i > 0:
    if i > 1:
        print(f'{i} x ', end='')
    else:
        print(f'{i} = ', end='')
    #decrementando variável contadora
    f *= i
    i -= 1
print(f)
print()
