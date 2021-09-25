

class DoesNotExist(Exception):
    pass


class Order:
    def __init__(self, coffe='', size='', milk='', location='', id=None):
        self.id = None if id is None else int(id)
        self.coffe = coffe
        self.size = size
        self.milk = milk
        self.location = location


class CoffeeShop:
    def __init__(self):
        self.orders = {}

    def place_order(self, order):
        if order.id is None:
            order.id = len(self.orders) + 1

        self.orders[order.id] = order
        return order

    def delete(self, order):
        try:
            return self.orders.pop(order.id)
        except KeyError as e:
            raise DoesNotExist(order.id)
