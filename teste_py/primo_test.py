def verificar_primo(n):
    raiz = int(n ** (0.5))
    #raiz+1 para incluir a própria raiz; pois range tem intervalo aberto
    for divisor in range(2, raiz+1):
        if n % divisor == 0:
            return False
    return True


def test_primo():
    assert verificar_primo(1) == True

def test_primo1():
    assert verificar_primo(4) == False

def test_primo2():
    assert verificar_primo(5) == True

def test_primo3():
    assert verificar_primo(17) == True

def test_primo4():
    assert verificar_primo(50) == False

def test_primo5():
    assert verificar_primo(787) == True

def test_primo6():
    assert verificar_primo(800) == False


####    explicação do uso da raiz   ####
# n = 2 * a
#    a = n / 2
#    pois não existe divisor que seja maior do que a metade do número ou menor do que ele mesmo
# n = a * b
#    b = n / a
# se a > raiz(n), então n/a < n/raiz(n)
#    efetuando os cálculos de radiciação para retitrar a raiz do denominador, temos
#    n/a < raiz(n), logo b < raiz(n)
