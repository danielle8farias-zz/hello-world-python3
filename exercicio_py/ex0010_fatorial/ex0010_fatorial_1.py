########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro e programa retorna o seu fatorial.
########

from time import sleep

num = int(input('Digite um número inteiro: '))
print(f'\nCalculando {num}!')
i = num
f = 1
sleep(0.5)
while i > 0:
    if i > 1:
        #end finalização da função print()
        #   não há quebra de linha
        #flush impede que o buffer segure a impressão por conta do sleep
        print(f'{i} x ', end='', flush=True)
        sleep(0.5)
    else:
        print(f'{i} = ', end='', flush=True)
        sleep(0.5)
    f *= i
    #decrementando variável contadora
    i -= 1
print(f)
print()
