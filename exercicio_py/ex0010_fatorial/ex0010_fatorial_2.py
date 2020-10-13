########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro e programa retorna o seu fatorial.
########

from time import sleep

num = int(input('Digite um número inteiro: '))
print(f'\nCalculando {num}!')
f = 1
sleep(0.5)
for i in range(num, 0, -1):
    #i vai assumir o valor de num dentro do laço
    if i > 1:
        print(f'{i} x ', end='', flush=True)
        sleep(0.5)
    else:
        print(f'{i} = ', end='', flush=True)
        sleep(0.5)
    f *= i
print(f)
print()
