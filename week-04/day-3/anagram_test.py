import unittest
from anagram_work import anagram

class TestAnagram(unittest.TestCase):
     def test_anagram(self):
        self.assertEqual(anagram("dog", "god"), True)

if __name__ == '__main__':
    unittest.main()