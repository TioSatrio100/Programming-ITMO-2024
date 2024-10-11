import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import lab2.caesar

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(lab2.caesar.encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(lab2.caesar.encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(lab2.caesar.encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(lab2.caesar.encrypt_caesar(""), "")

    def test_decrypt(self):
        self.assertEqual(lab2.caesar.decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(lab2.caesar.decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(lab2.caesar.decrypt_caesar("Sbwkrq3.6"), "Python3.6")
        self.assertEqual(lab2.caesar.decrypt_caesar(""), "")

    def test_custom_shift(self):
        self.assertEqual(lab2.caesar.encrypt_caesar("ABC", shift=1), "BCD")
        self.assertEqual(lab2.caesar.decrypt_caesar("BCD", shift=1), "ABC")
        self.assertEqual(lab2.caesar.encrypt_caesar("XYZ", shift=3), "ABC")
        self.assertEqual(lab2.caesar.decrypt_caesar("ABC", shift=3), "XYZ")

if __name__ == "__main__":
    unittest.main()


