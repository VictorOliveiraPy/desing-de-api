from http import HTTPStatus

from coopy.base import init_persistent_system
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from apps.level1.domain import Order, CoffeeShop

coffeeshop = init_persistent_system(CoffeeShop(), basedir='level1')


def barista(request):
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

    body = f'{order.id}'

    return HttpResponse(
        body,
        status=HTTPStatus.CREATED,
        headers={'Content-Type': 'text/plain; charset=utf8'}
    )
