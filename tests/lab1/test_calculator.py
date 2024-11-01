import unittest

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def times(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

class TestCalculator(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(2, 3), 5)
        self.assertEqual(plus(-1, 1), 0)

    def test_minus(self):
        self.assertEqual(minus(5, 2), 3)
        self.assertEqual(minus(0, 0), 0)

    def test_times(self):
        self.assertEqual(times(2, 3), 6)
        self.assertEqual(times(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(1, 1), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if  __name__ == '__main__':
    unittest.main()