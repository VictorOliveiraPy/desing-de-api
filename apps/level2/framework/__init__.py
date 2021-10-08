from django.urls import reverse

from .decorators import allow, datarequired, require
from .http import *
from .middleware import FrameworkCommonExceptionHandler
from .serializers import deserialize, serialize
from .tests import APIClient


def abs_reverse(request, viewname, args=None, kwargs=None, current_app=None):
    return request.build_absolute_uri(
        reverse(viewname, args=args, kwargs=kwargs, current_app=current_app)
    )
