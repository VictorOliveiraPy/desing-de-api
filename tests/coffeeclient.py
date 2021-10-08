import argparse
import json
import re

import requests

BASE_URL = 'http://localhost:8000'


# def place_order(coffee, size, milk, location):
#     url = f'{BASE_URL}/order/create?coffe{coffee}?size={size}?milk{milk}&location={location}'
#
#     r = requests.get(url)
#
#     return ''.join(re.findall(r'Order=(\d+)', r.text))


def post(coffee, size, milk, location):
    url = f'{BASE_URL}/order'
    data = dict(coffee=coffee, size=size, milk=milk, location=location)
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    return response.json()


def get(id):
    url = f'{BASE_URL}/order/{id}'
    headers = {'content-type': 'application/json'}

    response = requests.get(url, headers=headers)
    d = response.json()
    return d


def build_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    sp_order = subparsers.add_parser('order')
    sp_order.add_argument('coffee')
    sp_order.add_argument('size')
    sp_order.add_argument('milk')
    sp_order.add_argument('location')

    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    order = post(args.coffee, args.size, args.milk, args.location)

    print(order)

    print(get(id=order['id']))
