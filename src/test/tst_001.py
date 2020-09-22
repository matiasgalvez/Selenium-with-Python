import unittest


class FirstTest(unittest.TestCase):

    def set_up(self):
        self.a = 6
        self.b = 4

    def test_001(self):
        self.res = self.a + self.b

    def tear_down(self):
        self.assertTrue(self.res == 10, f"El valor de la no es 10, es {self.res}")
        self.assertFalse(self.res == 100, f"El valor de la no es 100, es {self.res}")
        self.assertEqual(10, self.res, f"El valor no es el esperado: {self.res}")


class SecondTest(unittest.TestCase):

    def set_up(self):
        self.a = "Resultado "
        self.b = "Esperado"

    def test_002(self):
        self.res = self.a + self.b

    def tear_down(self):
        self.assertTrue(self.res == "Resultado Esperado", f"El string no es {self.res}")
        self.assertFalse(self.res == "Resultado", "El string no es Resultado")
        self.assertEqual("Resultado Esperado", self.res, f"El string no es: {self.res}")


if __name__ == '__main__':
    unittest.main()
