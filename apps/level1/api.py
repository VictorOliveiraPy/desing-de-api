from coopy.base import init_persistent_system

from apps.level1.domain import CoffeeShop, DoesNotExist, Order
from apps.level1.framework import Created, NoContent, NotFound, allow, require

coffeeshop = init_persistent_system(CoffeeShop(), basedir='level1')


@allow(['POST'])
@require('coffe', 'size', 'milk', 'location')
def create(request, params):
    order = Order(**params)
    coffeeshop.place_order(order)

    body = f'Order={order.id}'

    return Created()


@allow(['POST'])
@require('id')
def delete(request, params):
    try:
        order = Order(**params)
        coffeeshop.delete(order)
    except DoesNotExist as e:
        return NotFound()

    return NoContent()
