import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("beer", 4, 5)
        self.drink_2 = Drink("wine", 5, 3)

        self.drinks = [self.drink, self.drink_2]
        self.customer = Customer("Dan", 20, 23)
        self.customer2 = Customer("Rab C", 2, 72)
        self.customer3 = Customer("Fred", 25, 17)
        self.customer4 = Customer("Jane", 40, 18)

    def test_customer_has_name(self):
        self.assertEqual("Dan", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_customer_pays_for_drink(self):
        self.customer.pay_for_drink(self.drink)
        self.assertEqual(16, self.customer.wallet)

    def test_customer_receives_drink(self):
        self.customer.receives_drink(self.drink)
        self.assertEqual(1, len(self.customer.drinks))

    def test_customer_buys_drink__True(self):
        pub = Pub("The Prancing Pony", 100, self.drinks)
        self.customer.buys_drink(self.drink, pub)
        self.assertEqual(1, len(self.customer.drinks))
        self.assertEqual(1, len(pub.drinks))
        self.assertEqual(16, self.customer.wallet)
        self.assertEqual(104, pub.money)

    def test_customer_buys_drink__False(self):
        pub = Pub("The Prancing Pony", 100, self.drinks)
        self.customer2.buys_drink(self.drink, pub)
        self.assertEqual(0, len(self.customer2.drinks))
        self.assertEqual(2, len(pub.drinks))
        self.assertEqual(2, self.customer2.wallet)
        self.assertEqual(100, pub.money)

    def test_customer_buys_drink_is_old_enough__False(self):
        pub = Pub("The Prancing Pony", 100, self.drinks)
        self.customer3.buys_drink(self.drink, pub)
        self.assertEqual(False, pub.check_customer_age(self.customer3))
        self.assertEqual(0, len(self.customer3.drinks))
        self.assertEqual(2, len(pub.drinks))
        self.assertEqual(25, self.customer3.wallet)
        self.assertEqual(100, pub.money)

    def test_customer_drunkeness(self):
        self.assertEqual(0, self.customer.drunkeness)

    def test_customer_has_drink_increase_drunkeness(self):
        self.customer.increase_drunkeness(self.drink)
        self.assertEqual(5, self.customer.drunkeness)

    def test_buys_drink_increase_drunk(self):
        pub = Pub("The Prancing Pony", 100, self.drinks)
        self.customer.buys_drink(self.drink, pub)
        self.assertEqual(1, len(self.customer.drinks))
        self.assertEqual(1, len(pub.drinks))
        self.assertEqual(16, self.customer.wallet)
        self.assertEqual(104, pub.money)
        self.assertEqual(5, self.customer.drunkeness)
