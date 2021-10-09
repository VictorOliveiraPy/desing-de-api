from enum import Enum, auto

from django.utils.datetime_safe import datetime


def now():
    return datetime.now()


class Status(Enum):
    Placed = auto()
    Paid = auto()
    Served = auto()
    Collected = auto()
    Cancelled = auto()


class Order:
    def __init__(self, coffee='', size='', milk='', location='', id=None, crated_at=None, status=None):
        self.id = None if id is None else int(id)
        self.coffee = coffee
        self.size = size
        self.milk = milk
        self.location = location
        self.created_at = now() if crated_at is None else crated_at
        self.status = status

    def vars(self):
        d = vars(self).copy()
        d['status'] = str(d['status']).removeprefix('Status.')
        return d

    def is_cancelled(self):
        return self.status == Status.Cancelled


class DoesNotExist(Exception):
    pass


class CoffeeShop:
    def __init__(self):
        self.orders = {}

    def create(self, order):
        if order.id is None:
            order.id = len(self.orders) + 1
        self.orders[order.id] = order
        return order

    def delete(self, id):
        id = int(id)
        try:
            order = self.orders[id]
        except KeyError as e:
            raise DoesNotExist(id)

        order.status = Status.Cancelled
        return order

    def update(self, order):
        saved = self.read(order.id)

        if order.status is None:
            order.status = saved.status

        self.orders[order.id] = order
        return order

    def read(self, id):
        id = int(id)
        try:
            return self.orders[id]
        except KeyError as e:
            raise DoesNotExist(id)
