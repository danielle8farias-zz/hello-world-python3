########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função recebe como argumentos o 1º termo de uma PA, sua razão e o número de termos.
# O programa calcula a soma de todos os termos dessa PA.
########

def pa_termo(A1, r, n):
    An = A1 + (n-1) * r
    return An


def pa_soma(A1, r, n):
    soma = 0
    for i in range(n+1):
        soma += pa_termo(A1, r, i)
    return soma


if __name__ == '__main__':
    print(pa_soma(2,2, 100))
    print(pa_soma(3,3,40))
