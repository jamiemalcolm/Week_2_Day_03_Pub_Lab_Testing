import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("beer", 4, 5)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(4, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(5, self.drink.alcohol_level)
