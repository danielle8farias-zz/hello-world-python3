def verificar_triangulo(lado1, lado2, lado3):
    if lado2+lado3 > lado1 and lado1+lado3 > lado2 and lado1+lado2 > lado3:
        if lado1 == lado2 and lado2 == lado3:
            return 'triângulo equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return 'triângulo isósceles'
        else:
            return 'triângulo escaleno'
    else:
        return 'não forma triângulo'


def test_triangulo():
    assert verificar_triangulo(3, 3, 3) == 'triângulo equilátero'

def test_triangulo1():
    assert verificar_triangulo(3, 3, 5) == 'triângulo isósceles'

def test_triangulo2():
    assert verificar_triangulo(3, 4, 5) == 'triângulo escaleno'

def test_triangulo3():
    assert verificar_triangulo(13, 3, 5) == 'não forma triângulo'
