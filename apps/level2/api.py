from coopy.base import init_persistent_system

from apps.level2.domain import CoffeeShop, Order
from apps.level2.framework import (Created, NoContent,
                                   Ok, allow, require)

coffeeshop = init_persistent_system(CoffeeShop(), basedir='level2')


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
    order = Order(**params)
    coffeeshop.delete(order)

    return NoContent()


@allow(['POST'])
@require('id', 'coffe', 'size', 'milk', 'location')
def update(request, params):
    order = Order(**params)
    order = coffeeshop.update(order)

    return NoContent()


@allow(['GET'])
@require('id')
def read(request, params):
    order = coffeeshop.read(**params)

    return Ok(str(order))
