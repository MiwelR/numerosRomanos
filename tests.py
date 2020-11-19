from numRomanos import *
import unittest

class RomanosTest(unittest.TestCase):

# TESTS PARA CONVERSIÓN DE NÚMEROS ROMANOS A ENTEROS:

    def test_I(self):
        self.assertEqual(romano_a_entero('I'), 1)
    
    def test_M(self):
        self.assertEqual(romano_a_entero('M'), 1000)
    
    def test_D(self):
        self.assertEqual(romano_a_entero('D'), 500)
    
    def test_C(self):
        self.assertEqual(romano_a_entero('C'), 100)
    
    def test_L(self):
        self.assertEqual(romano_a_entero('L'), 50)
    
    def test_X(self):
        self.assertEqual(romano_a_entero('X'), 10)
    
    def test_V(self):
        self.assertEqual(romano_a_entero('V'), 5)
    
    def test_J(self):
        self.assertRaises(ValueError, romano_a_entero, 'J')
    
    def test_23(self):
        self.assertRaises(ValueError, romano_a_entero, 23)
    
    def test_MMM(self):
        self.assertEqual(romano_a_entero('MMM'), 3000)
    
    def test_MMMM(self):
        self.assertRaises(ValueError, romano_a_entero, 'MMMM')
    
    def test_CC(self):
        self.assertEqual(romano_a_entero('CC'), 200)
    
    def test_III(self):
        self.assertEqual(romano_a_entero('III'), 3)
    
    def test_XX(self):
        self.assertEqual(romano_a_entero('XX'), 20)
    
    def test_VV(self):
        self.assertRaises(ValueError, romano_a_entero, 'VV')
    
    def test_repes_variadas(self):
        self.assertEqual(romano_a_entero('MMLXXIII'), 2073)
    
    def test_IV(self):
        self.assertEqual(romano_a_entero('IV'), 4)
    
    def test_IC(self):
        self.assertRaises(ValueError, romano_a_entero, 'IC')
    
    def test_MMMCMMM(self):
        self.assertRaises(ValueError, romano_a_entero, 'MMMCMMM')
    
    def test_IIX(self):
        self.assertRaises(ValueError, romano_a_entero, 'IIX')

# TESTS PARA CONVERSIÓN DE NÚMEROS ENTEROS A ROMANOS:

    def test_descomponer(self):
        self.assertEqual(descomponer(1987), [1,9,8,7])

    def test_descomponer_solo_enteros(self):
        self.assertRaises(SyntaxError, entero_a_romano, 1987.0)

    def test_convertir_987(self):
        self.assertEqual(convertir([9,8,7]), 'CMLXXXVII')

    def test_entero_a_romano(self):
        self.assertEqual(entero_a_romano(1987), 'MCMLXXXVII')
        self.assertRaises(OverflowError, entero_a_romano, 4000)
        self.assertRaises(OverflowError, entero_a_romano, 0)


if __name__ == '__main__':
    unittest.main()    