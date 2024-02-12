import unittest
from problem import check_nums

class TestSolution (unittest.TestCase):
    def test_true(self):
        self.assertEqual(check_nums(1,2), True, 'Answer is wrong')
        self.assertEqual(check_nums(15,17), True, 'Answer is wrong')

    def test_false(self):
        self.assertEqual(check_nums(5,1), False, 'Answer is wrong')
        self.assertEqual(check_nums(15,5), False, 'Answer is wrong')

    def test_equal(self):
        self.assertEqual(check_nums(6,6), -1, 'Answer is wrong')
        self.assertEqual(check_nums(3,3), -1, 'Answer is wrong')

if __name__ == '__main__':
    unittest.main()