########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o valor das raízes e programa retorna a qual equação do 2º grau elas pertencem.
########

#criando função que multiplica as raízes
def multip_raizes(x1, x2):
    #retorno da função
    return x1 * x2


def somar_raizes(x1, x2):
    #retorno da função
    return x1 + x2


def montar_equacao(x1, x2):
    #chamando funções dentro da função e guardando o retorno nas variáveis
    b = somar_raizes(x1, x2)
    c = multip_raizes(x1, x2)
    #sabendo-se que soma = -b e multiplicação = c; a = 1
    #   X² - bX + c

    #condicional

    #para b negativo
    #se b for um valor negativo e c for positivo
    if b < 0 and c > 0:
        #b*-1 para retirar o sinal negativo de b
        print(f'A equação é: X² + {b*-1}X + {c}')
    #else if
    #senão, se b for um valor negativo e c também
    elif b < 0  and c < 0:
        print(f'A equação é: X² + {b*-1}X - {c*-1}')
    #senão, se b for um valor negativo e c for igual a zero
    elif b < 0  and c == 0:
        print(f'A equação é: X² + {b*-1}X')

    #para b positivo
    #senão, se b for um valor positivo e c também
    elif b > 0 and c > 0:
        print(f'A equação é: X² - {b}X + {c}')
    #senão, se b for um valor positivo e c for negativo
    elif b > 0 and c < 0:
        print(f'A equação é: X² - {b}X - {c*-1}')
    #senão, se b for um valor positivo e c for igual a zero
    elif b > 0 and c == 0:
        print(f'A equação é: X² - {b}X')

    #para b igual a zero
    #senão, se b for um igual a zero e c for positivo
    elif b == 0 and c > 0:
        print(f'A equação é: X² + {c}')
    #senão, se b for um igual a zero e c for negativo
    elif b == 0 and c < 0:
        print(f'A equação é: X² - {c*-1}')
    #senão para b e c iguais a zero
    #   elif b == 0 and c == 0:
    else:
        print(f'A equação é: X²')


if __name__ == '__main__':
    #chamando função dentro da função
    montar_equacao(2, 3) #raízes
    montar_equacao(-2, -1)
    montar_equacao(3, 3)
    montar_equacao(-3, 2)
    montar_equacao(-1, 0)
    montar_equacao(0, 0)
