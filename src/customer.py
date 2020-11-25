from src.pub import Pub


class Customer():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.drinks = []
        self.age = age
        self.drunkeness = 0

    def pay_for_drink(self, drink):
        self.wallet -= drink.price

    def receives_drink(self, drink):
        self.drinks.append(drink)

    def buys_drink(self, drink, pub):
        if pub.check_customer_age(self) == True and self.wallet >= drink.price:
            self.receives_drink(drink)
            pub.gives_drink(drink)
            self.pay_for_drink(drink)
            pub.takes_payment(drink)
