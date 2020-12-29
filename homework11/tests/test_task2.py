from homework11.tasks.task2 import ElderDiscount, MorningDiscount, NoDiscount, Order


def test_order_without_discount():
    order = Order(100, NoDiscount)

    assert order.final_price() == 100


def test_order_with_a_morning_discount():
    order = Order(100, MorningDiscount)

    assert order.final_price() == 50


def test_order_with_a_elder_discount():
    order = Order(100, ElderDiscount)

    assert order.final_price() == 10
