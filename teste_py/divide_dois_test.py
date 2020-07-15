#função de dividir dois números
def dividir(n1, n2):
    return n1 / n2


#testes
def test_divide():
    assert dividir(4,2) == 2

def test_divide1():
    assert dividir(5,5) == 1

def test_divide2():
    assert dividir(27,3) == 9

def test_divide3():
    assert dividir(9,-3) == -3
