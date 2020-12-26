"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10

"""


class Discount:
    pass


class NoDiscount(Discount):
    def no_discount(self):
        return 0


class MorningDiscount(Discount):
    def morning_discount(self):
        return 0.5


class ElderDiscount(Discount):
    def elder_discount(self):
        return 0.9


class ListOfDiscounts:
    """Stores and distributes existing discount.

    Attributes:
        existing_discounts: Stores the discount name as a key and
        the discount path as a value.

    """

    existing_discounts = {
        "no_discount": NoDiscount.no_discount,
        "morning_discount": MorningDiscount.morning_discount,
        "elder_discount": ElderDiscount.elder_discount,
    }

    @staticmethod
    def requested_discount(discount):
        return ListOfDiscounts.existing_discounts[discount]


class Order:
    """Gets the order price and discount program.
    When calling the final_price method, the order price is returned.

    Args:
        price: The order price.
        discount_program: The desired discount program.

    Attributes:
        price: The order price.
        discount_program: The desired discount program.

    """

    def __init__(self, price, discount_program="no_discount"):
        self.price = price
        self.discount_program = discount_program

    def final_price(self):
        return self.price - self.price * ListOfDiscounts.requested_discount(
            self.discount_program
        )(self)


if __name__ == "__main__":
    order1 = Order(100)
    # print(order1.final_price())

    order2 = Order(100, "morning_discount")
    # print(order2.final_price())

    order3 = Order(100, "elder_discount")
    # print(order3.final_price())
