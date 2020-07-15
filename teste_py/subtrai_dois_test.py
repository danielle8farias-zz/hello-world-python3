#função de subtrair dois números
def subtrair(n1, n2):
    return n1 - n2


#testes
def test_subtracao():
    assert subtrair(3,2) == 1

def test_subtracao1():
    assert subtrair(5,5) == 0

def test_soma2():
    assert subtrair(7,2) == 5

def test_soma3():
    assert subtrair(9,-3) == 12
