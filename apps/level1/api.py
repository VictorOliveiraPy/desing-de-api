from http import HTTPStatus

from coopy.base import init_persistent_system
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from apps.level1.domain import Order, CoffeeShop, DoesNotExist

coffeeshop = init_persistent_system(CoffeeShop(), basedir='level1')


def create(request):
    if request.method != 'POST':
        return HttpResponse(
            HTTPStatus.METHOD_NOT_ALLOWED.description,
            status=HTTPStatus.METHOD_NOT_ALLOWED,
            headers={'Content-Type': 'text/plain; charset=utf-8'}
        )
    try:
        params = {
            k: request.GET[k]
            for k in (
                'coffe', 'size', 'milk', 'location'
            )
        }
    except MultiValueDictKeyError as e:
        return HttpResponse(
            str(e).strip("'"),
            status=HTTPStatus.BAD_REQUEST,
            headers={'Content-Type': 'text/plain; charset=utf-8'}
        )

    order = Order(**params)
    coffeeshop.place_order(order)

    body = f'Order={order.id}'

    return HttpResponse(
        body,
        status=HTTPStatus.CREATED,
        headers={'Content-Type': 'text/plain; charset=utf8'}
    )


def delete(request):
    if request.method != 'POST':
        return HttpResponse(
            HTTPStatus.METHOD_NOT_ALLOWED.description,
            status=HTTPStatus.METHOD_NOT_ALLOWED,
            headers={'Content-Type': 'text/plain; charset=utf-8'}
        )
    try:
        params = {
            k: request.GET[k]
            for k in ('id',)
        }
    except MultiValueDictKeyError as e:
        return HttpResponse(
            str(e).strip("'"),
            status=HTTPStatus.BAD_REQUEST,
            headers={'Content-Type': 'text/plain; charset=utf-8'}
        )
    try:
        order = Order(**params)
        coffeeshop.delete(order)
    except DoesNotExist as e:
        return HttpResponse(
            status=HTTPStatus.NOT_FOUND,
            headers={'Content-Type': 'text/plain; charset=utf-8'}
        )

    return HttpResponse(status=HTTPStatus.NO_CONTENT, headers={'Content-Type': 'text/plain; charset=utf-8'})