import pytest

from apps.level1.domain import CoffeeShop, Order


@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('apps.level1.api.coffeeshop', cs)
    return cs

@pytest.fixture
def order():
   return Order(coffe='latte', size='large', milk='whole', location='takeAway')




@pytest.fixture
def onecoffee(coffeeshop, order):
    coffeeshop.place_order(order)
    return coffeeshop
