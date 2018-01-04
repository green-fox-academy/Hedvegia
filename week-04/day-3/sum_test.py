import unittest
from sum_work import Summa

my_list = Summa()

class TestSum(unittest.TestCase):
     def test_sum(self):
        self.assertEqual(my_list.sum_my_list([1, 2, 3, 4]), 10)

if __name__ == '__main__':
    unittest.main()