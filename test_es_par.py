import unittest
from math_utils import es_par #aun no existe pero queremos que falle

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))

    def test_5_no_es_par(self):
        self.assertFalse(es_par(5))

    def test_0_es_par(self):
        self.assertTrue(es_par(0))

    def test_negativos(self):
        self.assertTrue(es_par(-2))

if __name__ == "main":
    unittest.main()