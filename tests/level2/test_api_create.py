from http import HTTPStatus

import pytest


def test_get_not_allowed(client, coffeeshop):
    url = '/order/create'
    data = dict(coffe='latte', size='large', milk='whole', location='takeAway')
    response = client.get(url, data=data, content_type='application/json')

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeeshop.orders) == 0


def test_post_sucess(client, coffeeshop):
    url = '/order/create'
    data = dict(coffe='latte', size='large', milk='whole', location='takeAway')

    response = client.post(url, data=data, content_type='application/json')

    assert response.status_code == HTTPStatus.CREATED
    assert len(coffeeshop.orders) == 1
    assert response.content == b'coffee=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'


@pytest.mark.skip
def test_post_badreq(client, coffeeshop):
    url = '/order/create'
    data = dict(coffe='latte', size='large', milk='whole')

    response = client.post(url, data=data, content_type='application/json')
