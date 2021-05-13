########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: O programa recebe dois ou mais números inteiros e retorna o máximo divisor comum deles.
########

def calcular_mdc(a, b):
    # o mesmo que while != 0
    # while 0 = False
    while b:
        a, b = b, a%b
    return a


def mdc(lista_num):
    if len(lista_num) == 2:
        return calcular_mdc(lista_num[0], lista_num[1])
    else:
        # calcula o mdc de dois em dois
        mdc_valor = calcular_mdc(lista_num[0], lista_num[1])
        lista_num[0] = mdc_valor
        # deleta a segunda posição que já foi utilizada
        del lista_num[1]
        # recursão
        return mdc(lista_num)


if __name__ == '__main__':
    print(mdc([180, 240, 270])) # 30
    print(mdc([540, 810, 1080])) # 270
    print(mdc([80, 100, 120])) # 20
    print(mdc([30, 36, 48])) # 6
    print(mdc([20, 36])) # 4
