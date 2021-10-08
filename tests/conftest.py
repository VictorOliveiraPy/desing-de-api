import pytest
from pytest_django.lazy_django import skip_if_no_django

from apps.level2 import domain
from apps.level2.domain import CoffeeShop, Order, Status
from apps.level2.framework import APIClient


@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('apps.level2.api.coffeeshop', cs)
    return cs


@pytest.fixture
def order():
    return Order(coffee='latte', size='large', milk='whole', location='takeAway',
                 status=Status.Placed)


@pytest.fixture
def onecoffee(coffeeshop, order):
    coffeeshop.create(order)
    return coffeeshop


@pytest.fixture
def apiclient():
    skip_if_no_django()

    return APIClient()


@pytest.fixture(autouse=True)
def fixed_now(monkeypatch):
    from datetime import datetime
    monkeypatch.setattr(domain, 'now', lambda: datetime(2021, 4, 28))
