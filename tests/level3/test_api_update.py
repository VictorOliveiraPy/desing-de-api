from datetime import datetime
from http import HTTPStatus

import pytest


def test_update_success(apiclient, onecoffee):
    url = '/order/1'
    data = dict(coffee='curto', milk='', size='small', location='takeAway')
    response = apiclient.put(url, data=data)

    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1'
    )
    expected = dict(
        id=1, coffee='curto', milk='', size='small', location='takeAway', created_at=datetime(2021, 4, 28),
        status='Placed', links=links
    )
    assert response.status_code == HTTPStatus.OK
    assert len(onecoffee.orders) == 1
    assert response.json() == expected


@pytest.mark.skip
def test_update_not_allowed(client, onecoffee):
    url = '/order/update?id=1&coffe=curto&milk=&size=small&location=takeAway'
    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_update_badreq(apiclient, onecoffee):
    url = '/order/1'
    data = dict(coffee='curto', milk='', size='small')
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(onecoffee.orders) == 1


def test_update_not_found(apiclient, onecoffee):
    url = '/order/404&coffee=curto&milk=&size=small&location=takeAway'
    data = dict(coffee='curto', milk='', size='small', location='takeAway')
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.NOT_FOUND
