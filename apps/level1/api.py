from coopy.base import init_persistent_system

from apps.level1.domain import CoffeeShop, DoesNotExist, Order
from apps.level1.framework import (Created, MyResponse, NoContent, NotFound,
                                   Ok, allow, require)

coffeeshop = init_persistent_system(CoffeeShop(), basedir='level1')


@allow(['POST'])
@require('coffe', 'size', 'milk', 'location')
def create(request, params):
    order = Order(**params)
    coffeeshop.create(order)

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


@allow(['POST'])
@require('id', 'coffe', 'size', 'milk', 'location')
def update(request, params):
    try:
        order = Order(**params)
        order = coffeeshop.update(order)
    except DoesNotExist as e:
        return NotFound()

    return NoContent()


@allow(['GET'])
@require('id')
def read(request, params):
    try:
        order = coffeeshop.read(**params)
    except DoesNotExist as e:
        return NotFound()

    return Ok(str(order))
