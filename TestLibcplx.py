import Libcplx as lc
import unittest

class TestCplxOperations (unittest.TestCase):

    def test_sumacplx(self):
        suma = lc.sumacplx((3,2),(-5,5.2))
        self.assertAlmostEqual(suma[0], -2)
        self.assertAlmostEqual(suma[1],7.2)

        suma = lc.sumacplx((5, 2), (4, 7))
        self.assertAlmostEqual(suma[0], 9)
        self.assertAlmostEqual(suma[1], 9)

    def test_restacplx(self):
        resta= lc.restacplx ((3,2),(-5,5.2))
        self.assertAlmostEqual(resta[0], 8)
        self.assertAlmostEqual(resta[1], -3.2)

        resta = lc.restacplx((5, 2), (-1, -3.5))
        self.assertAlmostEqual(resta[0], 6)
        self.assertAlmostEqual(resta[1], 5.5)


    def test_multcplx(self):
        multiplicar = lc.multcplx ((3,2),(-5,5.2))
        self.assertAlmostEqual(multiplicar[0], -25.4)
        self.assertAlmostEqual(multiplicar[1], 5.6, places = 1)


        multiplicar = lc.multcplx((-6, -1), (-3, -5))
        self.assertEqual(multiplicar[0], 13)
        self.assertEqual(multiplicar[1], 33)

    def test_divisioncplx(self):
        dividir = lc.divisioncplx ((3,2),(-5,5.2))
        self.assertAlmostEqual(dividir[0], -0.08, places = 1)
        self.assertAlmostEqual(dividir[1], -0.49, places = 1)

        dividir = lc.divisioncplx((-4, 5), (8, -2))
        self.assertAlmostEqual(dividir[0], -0.61, places = 1)
        self.assertAlmostEqual(dividir[1], 0.47, places = 1)


    def test_modulocplx(self):
        modulo = lc.modulocplx((3, 2))
        self.assertAlmostEqual(modulo, 3.60, places= 1)

        modulo = lc.modulocplx((4.5, 3.63))
        self.assertAlmostEqual(modulo, 5.78, places=1)

    def test_conjugadocplx(self):
        conjugado = lc.conjugadocplx((3, 2))
        self.assertAlmostEqual(conjugado[0], 3)
        self.assertAlmostEqual(conjugado[1], -2)

        conjugado = lc.conjugadocplx((-4, 5))
        self.assertAlmostEqual(conjugado[0], -4)
        self.assertAlmostEqual(conjugado[1], -5)

    def test_cartpolarcplx(self):
        coordenada = lc.cartpolarcplx((-9, 4))
        self.assertAlmostEqual(coordenada[0], 9.84, places= 1)
        self.assertAlmostEqual(coordenada[1], -0.41, places=1)

        coordenada = lc.cartpolarcplx((2, 6))
        self.assertAlmostEqual(coordenada[0], 6.32, places=1)
        self.assertAlmostEqual(coordenada[1], 1.24, places=1)


    def test_fasecplx(self):
        fase = lc.fasecplx((3, 2))
        self.assertAlmostEqual(fase, 0.58, places= 1)

        fase = lc.fasecplx((-9, 4))
        self.assertAlmostEqual(fase, -0.41, places=1)


if __name__ == '__main__':
    unittest.main()

