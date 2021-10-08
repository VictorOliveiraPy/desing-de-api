import functools
from django.test import Client
from functools import partialmethod
from apps.level2.framework.http import DEFAULT_CT
from apps.level2.framework.serializers import MyJSONEncoder, MyJSONDecoder

APIClient = type(
    'APIClient',
    (Client,),
    {
        '__init__': partialmethod(Client.__init__, json_encoder=MyJSONEncoder),
        '_parse_json': partialmethod(Client._parse_json, cls=MyJSONDecoder),
        **{verb: partialmethod(getattr(Client, verb), content_type=DEFAULT_CT)
           for verb in ('post', 'get', 'put', 'delete')},
    }
)
