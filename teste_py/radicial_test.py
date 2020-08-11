def radiciar(indice, radicando):
    #retorna negativo se índice ímpar e radicando negativo
    if radicando < 0 and indice % 2 == 1:
        radicando *= -1
        raiz = radicando ** (1/indice)
        return round(raiz * -1, 5)
    
    elif (indice % 2 == 0 or indice % 2 == 1) and radicando > 0:
        raiz = radicando ** (1/indice)
        return round(raiz, 5)
    
    else:
        return 'Não é possível calcular a raiz dentro dos Reais.'


def test_radicial():
    assert radiciar(3, 64) == 4

def test_radicial1():
    assert radiciar(2, 64) == 8

def test_radicial2():
    assert radiciar(2, -25) == 'Não é possível calcular a raiz dentro dos Reais.'

def test_radicial3():
    assert radiciar(3, -27) == -3

def test_radicial4():
    assert radiciar(2, 7) == 2.64575
