from math import radians, sin, cos, tan

def seno(n):
    return sin(radians(n))


def cosseno(n):
    return cos(radians(n))


def tangente(n):
    return tan(radians(n))


#testes
def test_seno():
    assert seno(30) == 0.49999999999999994 #seria 0.5

def test_cosseno():
    assert cosseno(30) == 0.8660254037844387

def test_tangente():
    assert tangente(30) == 0.5773502691896257
