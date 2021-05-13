########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: O programa recebe dois números inteiros e retorna o máximo divisor comum.
########

def mdc(a, b):
    #caso o primeiro número seja menor do que o segundo, faz-se a troca
    if a < b:
        a,b = b,a

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

if __name__ == '__main__':
    print(mdc(20,36)) # 4
    print(mdc(90,54)) # 18
    print(mdc(400,320)) # 80

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