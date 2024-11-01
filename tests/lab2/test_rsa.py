import unittest
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from lab2.rsa import is_prime, gcd, multiplicative_inverse

class TestRSAFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(29))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(20, 30), 10)
        self.assertEqual(gcd(17, 19), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(3, 11), 4)

if __name__ == '__main__':
    unittest.main()
