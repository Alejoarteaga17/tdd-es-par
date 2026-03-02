import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase):
    
    def test_sumar_positivos(self):
        self.assertEqual(sumar(3,5),8)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-1,-3),-4)
    

if __name__ == '__main__':
    unittest.main()