from homework11.tasks.task2 import Order


def test_order_without_discount():
    order = Order(100)

    assert order.final_price() == 100


def test_order_with_a_morning_discount():
    order = Order(100, "morning_discount")

    assert order.final_price() == 50


def test_order_with_a_elder_discount():
    order = Order(100, "elder_discount")

    assert order.final_price() == 10
