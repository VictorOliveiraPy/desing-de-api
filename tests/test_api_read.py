from http import HTTPStatus


def test_read_success(client, onecoffee):
    url = '/order?id=1'
    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.content == b'coffe=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'


def rest_read_not_allowed(client, onecoffe):
    url = '/order?id=1'
    response = client.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_read_badreq(client, onecoffee):
    url = '/order'
    response = client.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_not_found(client, onecoffee):
    url = '/order?id=404'
    response = client.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND