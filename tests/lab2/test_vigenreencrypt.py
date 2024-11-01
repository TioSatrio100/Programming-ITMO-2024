import unittest
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from lab2.vigenre import encrypt_vigenre

class TestEncryptVigenre(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt_vigenre("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenre("python", "a"), "python")
        self.assertEqual(encrypt_vigenre("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenre("HELLO, WORLD!", "KEY"), "RIJVS, UYVJN!")

if __name__ == '__main__':
    unittest.main()
