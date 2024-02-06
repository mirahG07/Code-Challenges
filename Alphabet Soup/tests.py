import unittest
from problem import alphabet_soup

class TestSolution(unittest.TestCase):
    def test_lower_case(self):
        self.assertEqual(alphabet_soup("zxyw"),"wxyz", f'Wrong: got {alphabet_soup("zxyw")}')
        self.assertEqual(alphabet_soup("goodluck"), "cdgkloou", f'Wrong: got {alphabet_soup("goodluck")}')
    def test_upper_case(self):
        self.assertEqual(alphabet_soup("ZYWX"),"wxyz", f'Wrong: got {alphabet_soup("ZYWX")}')
        self.assertEqual(alphabet_soup("GOODLUCK"), "cdgkloou", f'Wrong: got {alphabet_soup("GOODLUCK")}')
    def test_with_symbols(self):
        self.assertEqual(alphabet_soup("ZYWX!?"),"wxyz", f'Wrong: got {alphabet_soup("ZYWX")}')
        self.assertEqual(alphabet_soup("Good luck!"), "cdgkloou", f'Wrong: got {alphabet_soup("GOODLUCK")}')
if __name__ == "__main__":
    unittest.main()