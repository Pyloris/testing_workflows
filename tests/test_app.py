import unittest

from app import add_num, sub_num, mul_num

class TestCode(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_num(2,3), 5)
    
    def test_sub(self):
        self.assertEqual(sub_num(5,10), -5)
    
    def test_mul(self):
        self.assertEqual(mul_num(6,6), 36)


if __name__ == "__main__":
    unittest.main()