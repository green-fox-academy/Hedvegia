import unittest
from fibonacci_work import fibonacci

class TestFibonacci(unittest.TestCase):
     def test_fibonacci(self):
        self.assertEqual(fibonacci(9), 34)

if __name__ == '__main__':
    unittest.main()