def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False


def test_bissexto():
    assert ano_bissexto(2020) == True

def test_bissexto1():
    assert ano_bissexto(2018) == False

def test_bissexto2():
    assert ano_bissexto(2016) == True

def test_bissexto3():
    assert ano_bissexto(2000) == True
