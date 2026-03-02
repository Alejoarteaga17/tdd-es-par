import pytest
from calculadora import sumar, dividir

def test_sumar_positivos():
    assert sumar(3,5) == 8

def test_sumar_negativos():
    assert sumar(-1,-3) == -4

def test_dividir_normal():
    assert dividir(10,4) == 2,5

def test_dividir_cero():
    assert dividir(5,0) == 1