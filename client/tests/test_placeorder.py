import httpretty

from client.core import place_order


@httpretty.activate
def test_place_order():
    httpretty.register_uri(
        httpretty.GET,
        'http://localhost:8000/PlaceOrder',
        'Order=1'
    )
    assert place_order('latte', 'whole', 'large', 'takeAway') == '1'
