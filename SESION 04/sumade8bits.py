import unittest

def add(a0, b0, c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    return s1, c1

class TestAdd(unittest.TestCase):

    def test_case_000(self):
        self.assertEqual(add(False, False, False), (False, False))

    def test_case_001(self):
        self.assertEqual(add(False, False, True), (True, False))

    def test_case_010(self):
        self.assertEqual(add(False, True, False), (True, False))

    def test_case_011(self):
        self.assertEqual(add(False, True, True), (False, True))

    def test_case_100(self):
        self.assertEqual(add(True, False, False), (True, False))

    def test_case_101(self):
        self.assertEqual(add(True, False, True), (False, True))

    def test_case_110(self):
        self.assertEqual(add(True, True, False), (False, True))

    def test_case_111(self):
        self.assertEqual(add(True, True, True), (True, True))

if __name__ == '__main__':
    unittest.main()