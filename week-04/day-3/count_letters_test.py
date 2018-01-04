import unittest
from count_letters_work import count_letters

class TestMyLetters(unittest.TestCase):
     def test_myLetters(self):
        self.assertEqual(count_letters("dog"), 3)

if __name__ == '__main__':
    unittest.main()