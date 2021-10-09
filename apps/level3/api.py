from coopy.base import init_persistent_system

from apps.level3.domain import CoffeeShop, Order, Status
from apps.level3.framework import (Created, NoContent, Ok, abs_reverse, allow,
                                   datarequired, serialize)

coffeeshop = init_persistent_system(CoffeeShop(), basedir='level3')


@allow('GET', 'POST', 'PUT', 'DELETE')
def dispatch(request, *args, **kwargs):
    methods = dict(GET=read, POST=create, PUT=update, DELETE=delete)
    view = methods[request.method]

    return view(request, *args, **kwargs)


@allow('POST')
@datarequired('coffee', 'size', 'milk', 'location')
def create(request, params=None):
    order = Order(**params, status=Status.Placed)
    coffeeshop.create(order)

    d = order.vars()
    link_to_self = abs_reverse(request, 'order', args=(order.id,))
    d['links'] = dict(
        self=link_to_self,
        update=link_to_self,
        cancel=link_to_self,
        payment=abs_reverse(request, 'payment', args=(order.id,))
    )

    return Created(
        serialize(d),
        headers={'Location': abs_reverse(request, 'order', args=(order.id,))}
    )


@allow('DELETE')
def delete(request, id):
    order = coffeeshop.delete(id=id)

    return NoContent()


@allow('PUT')
@datarequired('coffee', 'size', 'milk', 'location')
def update(request, id, params=None):
    order = Order(id=id, **params)
    order = coffeeshop.update(order)

    d = order.vars()
    link_to_self = abs_reverse(request, 'order', args=(order.id,))
    d['links'] = dict(
        self=link_to_self,
        update=link_to_self,
        cancel=link_to_self,
        payment=abs_reverse(request, 'payment', args=(order.id,))
    )
    return Ok(serialize(d))


@allow('GET')
def read(request, id):
    order = coffeeshop.read(id)

    return Ok(serialize(order))


def payment(request, id):
    return Ok()
