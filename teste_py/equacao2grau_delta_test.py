#função que calcula o delta de uma equação do 2º grau
def calcular_delta(a, b, c):
    delta = (pow(b, 2)) - 4 * a * c
    return delta


#testes
def teste_delta():
    assert calcular_delta(3, -7, 4) == 1

def teste_delta1():
    assert calcular_delta(9, -12, 4) == 0

def teste_delta2():
    assert calcular_delta(5, 3, 5) == -91

def teste_delta3():
    assert calcular_delta(2, 1, -3) == 25
