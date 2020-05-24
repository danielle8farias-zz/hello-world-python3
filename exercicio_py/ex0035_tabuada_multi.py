'''
Usuário digita um número e programa retorna a tabuada de multiplicação desse número, usando o laço for.
'''

num = float(input('Digite um número: '))

i = 1
for i in range(i, 10):
    print(f'{num:4} x {i} = {num*i}')
print()
