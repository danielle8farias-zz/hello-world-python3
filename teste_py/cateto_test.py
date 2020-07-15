from math import sqrt

#dado um cateto e a hipotenusa, retorna o valor do outro cateto
def calcular_cateto(a, b):
    c = sqrt(a**2 - pow(b, 2))
    return c


#testes
def test_cateto():
    assert calcular_cateto(5, 4) == 3

def test_cateto1():
    assert calcular_cateto(5, 3) == 4

def test_cateto2():
    assert calcular_cateto(30,15) == 25.98076211353316

def test_cateto3():
    assert calcular_cateto(25, 24) == 7
