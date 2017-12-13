import unittest
from apple_work import *

class TestStringApple(unittest.TestCase):
     def test_get_apple(self):
        self.assertEqual(apple.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()