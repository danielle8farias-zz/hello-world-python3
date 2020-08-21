#função que calcula as raízes de uma equação do 2º grau
def calcular_raizes(a, b, raiz_delta):
    x1 = (-b + raiz_delta)/(2 * a)
    x2 = (-b - raiz_delta)/(2 * a)
    return x1, x2


#testes
def teste_calcula_raizes():
    assert calcular_raizes(5, -3, 7) == (1.0, -0.4)

def teste_calcula_raizes1():
    assert calcular_raizes(2, 3, 7) == (1.0, -2.5)

def teste_calcula_raizes2():
    assert calcular_raizes(2, -9, 5) == (3.5, 1)
