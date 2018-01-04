import unittest
from sharpie_work import *    

sharpie = Sharpie("blue", 20)

class TestSharpie(unittest.TestCase):

    def test_sarpie(self):
        self.assertEqual(sharpie.use(), 99)

if __name__ == '__main__':
    unittest.main()