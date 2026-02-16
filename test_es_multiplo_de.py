import unittest
from math_utils import es_multiplo_de #aun no existe pero queremos que falle

class TestEsMultiplo(unittest.TestCase):
    def test_4_multiplo_de_2(self):
        self.assertTrue(es_multiplo_de(4, 2))
    def test_7_no_es_multiplo_3(self):
        self.assertFalse(es_multiplo_de(7, 3))
    def test_negativos(self):
        self.assertFalse(es_multiplo_de(-7, 14))

if __name__ == "main":
    unittest.main()