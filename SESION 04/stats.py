import unittest
import math

def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1):
        if number % check == 0:
            return False
    return True

def isPrime2(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:  # <- CORRECTO AQUÍ
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

class TestPrimes(unittest.TestCase):

    def test_isPrime_basic(self):
        self.assertFalse(isPrime(1))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertFalse(isPrime(4))
        self.assertTrue(isPrime(5))

    def test_isPrime_more(self):
        self.assertFalse(isPrime(20))
        self.assertFalse(isPrime(21))
        self.assertFalse(isPrime(22))
        self.assertTrue(isPrime(23))
        self.assertFalse(isPrime(24))

    def test_isPrime2_basic(self):
        self.assertFalse(isPrime2(1))
        self.assertTrue(isPrime2(2))
        self.assertTrue(isPrime2(3))
        self.assertFalse(isPrime2(4))
        self.assertTrue(isPrime2(5))

    def test_isPrime2_more(self):
        self.assertFalse(isPrime2(20))
        self.assertFalse(isPrime2(21))
        self.assertFalse(isPrime2(22))
        self.assertTrue(isPrime2(23))
        self.assertFalse(isPrime2(24))

    def test_isPrime2_error_detection(self):
        self.assertFalse(isPrime2(9))  

if __name__ == "__main__":
    unittest.main()
