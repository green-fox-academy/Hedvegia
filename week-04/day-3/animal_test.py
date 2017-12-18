import unittest
from animal_work import *    

animal = Animal()

class TestAnimal(unittest.TestCase):
    
    def test_animal_eat(self):
        self.assertEqual(animal.eat(), 49)

    def test_animal_drink(self):
        self.assertEqual(animal.drink(), 49)

    def test_animal_play(self):
        self.assertEqual(animal.play(), [50, 50])        

if __name__ == '__main__':
    unittest.main()