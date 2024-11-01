import unittest
from lab2.vigenre import decrypt_vigenere

class TestDecryptVigenere(unittest.TestCase):

    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

if __name__ == '__main__':
    unittest.main()
