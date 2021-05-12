########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: O programa recebe dois números inteiros e retorna o máximo divisor comum.
########

# usando recursão
def mdc(a, b):
    # caso o primeiro número seja menor do que o segundo, faz-se a troca na chamada da função
    if a < b:
        return mdc(b,a)

    # se b = 0, 'a' é o maior divisor comum
    if b == 0:
        return a
    r = a % b
    # 'b' ocupando o lugar de 'a'
    # 'r' ocupando o lugar de 'b'
    return mdc(b,r)


if __name__ == '__main__':
    print(mdc(20,36))
    print(mdc(90,54))
    print(mdc(400,320))

####        EXPLICAÇÃO PARA O USO DE R=A%B      ####
# MDC(a,b) =  MDC(a-b,b) para a > b
# se (a-b) > b, então MDC(a-b,b) = MDC(a-b-b,b)
# MDC(a-b,b) = MDC(a-2b,b) e assim por diante, ou seja
# MDC(a,b) = MDC(a-b,b) = MDC(a-2b,b) = ...
# a = q * b + r
# 'a' é igual ao quociente 'q' vezes 'b', mais o resto da divisão 'r'
# a/b tem resto 'r' e quociente 'q'
# r = a - q * b
# MDC (a,b) = MDC(a-q*b,b) = MDC(r,b)
# quando o 'r' = 0, então sabemos que 'b' é o maior divisor comum
#
########