from coopy.base import init_persistent_system
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from apps.core.domain import Order, CoffeShop

coffeshop = init_persistent_system(CoffeShop())


def barista(request):
    """
    http://localhost:800/placeOrder?coffe=latte&size=large&milk=whole&location=takeAway
    - Erro com status code 200. Trocar para BadRequest.
    - Get com efeito colateral.
    - Impossivel de cachear

    """
    try:
        params = {
            k: request.GET[k]
            for k in (
                'coffe', 'size', 'milk', 'location'
            )
        }

    except MultiValueDictKeyError as e:
        key = str(e).strip("'")
        body = f'Missing Param: {key}'
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        return HttpResponse(body, status=400, headers=headers)

    order = Order(**params)
    coffeshop.place_order(order)

    body = f'{order.id}'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}

    return HttpResponse(body, headers=headers)
