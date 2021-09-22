from apps.level1.domain import CoffeeShop
import pytest

@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('apps.level1.api.coffeeshop', cs)
    return cs
