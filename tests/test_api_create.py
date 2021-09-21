from http import HTTPStatus

from domain import CoffeShop

import pytest

def coffeshop(mocker):
    cs = CoffeShop()
    mocker.patch('apps.level1.api.coffeshop', cs)
    return cs


def test_get_not_allowed(client, coffeshop):
    url = '/order/create?coffe=latte&size=large&milk=whole&location=takeAway'
    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeshop) == 0


def test_post_sucess(client, coffeshop):
    url = '/order/create?coffe=latte&size=large&milk=whole&location=takeAway'
    response = client.post(url)

    assert response.status_code == HTTPStatus.CREATED
    assert len(coffeshop.orders) == 1
    assert b'Order=1' == response.content


def test_post_badreq(client, coffeshop):
    url = '/order/create?coffe=latte&size=large&milk=whole'
    response = client.post(url)
