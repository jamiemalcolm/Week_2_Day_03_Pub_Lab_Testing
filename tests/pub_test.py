# tests/pub_test.py

import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("beer", 4, 5)
        self.drink_2 = Drink("wine", 5, 4)

        self.drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("The Prancing Pony", 100, self.drinks)

        self.customer_1 = Customer("Fred", 25, 17)
        self.customer_2 = Customer("Jane", 40, 18)

    def test_check_customer_age__False(self):
        self.pub.check_customer_age(self.customer_1)
        self.assertEqual(False, self.pub.check_customer_age(self.customer_1))

    def test_check_customer_age__True(self):
        self.pub.check_customer_age(self.customer_2)
        self.assertEqual(True, self.pub.check_customer_age(self.customer_2))

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_drink(self):
        self.assertEqual(2, len(self.drinks))

    def test_pub_takes_payment(self):
        self.pub.takes_payment(self.drink_1)
        self.assertEqual(104, self.pub.money)

    def test_pub_gives_drink(self):
        self.pub.gives_drink(self.drink_1)
        self.assertEqual(1, len(self.drinks))
