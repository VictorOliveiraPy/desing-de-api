import httpretty

from clientes.client_level0.core import place_order


@httpretty.activate
def test_place_order():
    httpretty.register_uri(
        httpretty.GET,
        'http://localhost:8000/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAway',
        'Order=1',
        match_querystring=True
    )
    assert place_order(coffee='latte', size='large', milk='whole', location='takeAway') == '1'
