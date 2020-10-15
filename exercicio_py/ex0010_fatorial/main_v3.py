########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro e programa retorna o seu fatorial.
########

def fat(n):
    if n == 1 or n == 0:
        return 1
    #recursão
    return fat(n-1) * n

num = int(input('Digite um número: '))
print(fat(num))
