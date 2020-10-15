########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita um número natural inteiro e programa verifica se esse é número primo.
########

def verificar_primo(n):
    raiz = int(n ** (0.5))
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
