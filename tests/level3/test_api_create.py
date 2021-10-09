from datetime import datetime
from http import HTTPStatus

import pytest


@pytest.mark.skip
def test_get_not_allowed(client, coffeeshop):
    url = '/order/create'
    data = dict(coffe='latte', size='large', milk='whole', location='takeAway')
    response = client.get(url, data=data, content_type='application/json')

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeeshop.orders) == 0


def test_post_sucess(apiclient, coffeeshop):
    url = '/order'
    data = dict(coffee='latte', size='large', milk='whole', location='takeAway')
    response = apiclient.post(url, data=data)
    assert response.status_code == HTTPStatus.CREATED

    assert response.headers['Location'] == 'http://testserver/order/1'
    assert len(coffeeshop.orders) == 1

    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1'
    )

    expected = dict(id=1, coffee='latte', size='large', milk='whole', location='takeAway',
                    created_at=datetime(2021, 4, 28), status='Placed', links=links)
    assert response.json() == expected


def test_post_badreq(client, coffeeshop):
    url = '/order'
    data = dict(coffe='latte', size='large', milk='whole')

    response = client.post(url, data=data, content_type='application/json')
