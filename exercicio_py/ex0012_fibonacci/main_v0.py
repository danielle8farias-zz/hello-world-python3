########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro e programa retorna a sequência de Fibonacci dos n elementos lidos.
########

num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')

i = 3
while i <= num:
    tn = t1 + t2
    print(f' -> {tn}', end='')
    #atualizando os valores dos termos
    t1, t2 = t2, tn
    i += 1
print()
