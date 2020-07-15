#função de multiplicar dois números
def multiplicar(n1, n2):
    return n1 * n2


#testes
def test_multiplica():
    assert multiplicar(1,2) == 2

def test_multiplica1():
    assert multiplicar(5,5) == 25

def test_multiplica2():
    assert multiplicar(7,2) == 14

def test_multiplica3():
    assert multiplicar(9,-3) == -27
