########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função recebe como argumentos o 1º termo de uma PA, sua razão e o número de termos.
# O programa calcula a soma de todos os termos dessa PA.
########

def pa_termo(A1, r, n):
    An = A1 + (n-1) * r
    return An


def pa_soma(A1, An, n):
    soma = (A1 + An) * n/2
    return soma


if __name__ == '__main__':
    An = pa_termo(2, 2, 100)
    print(pa_soma(2, An, 100))
    
    An = pa_termo(3, 3, 40)
    print(pa_soma(3, An, 40))
