import unittest


class FirstTest(unittest.TestCase):

    def set_up(self):
        pass

    def test_002(self):
        self.a = 1
        self.b = 1
        self.res = self.a + self.b

        self.assertEqual(self.a, self.b, f'{self.a} no es igual a {self.b}')

    def test_003(self):
        self.a = 1
        self.b = 2
        self.res = self.a + self.b

        self.assertNotEqual(self.a, self.b, f'{self.a} no es igual a {self.b}')

    def test_004(self):
        self.a = 10
        if self.a >= 10:
            self.Resultado = True
        else:
            self.Resultado = False

        self.assertTrue(self.Resultado, f'{self.Resultado} no es true')

    def test_004(self):
        self.a = 'Mundo'
        self.b = 'Hola Mundo'
        self.assertIn(self.a, self.b, 'No coinciden')

    def tear_down(self):
        pass


if __name__ == '__main__':
    unittest.main()