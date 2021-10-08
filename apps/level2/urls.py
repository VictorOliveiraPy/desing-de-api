from django.urls import path, re_path

from . import api

urlpatterns = [
    re_path(r'order(?:/(?P<id>\d+))?', api.dispatch, name='order'),
    # path('order/create', api.create),
    # path('order/delete', api.delete),
    # path('order/update', api.update),
    # path('order', api.read),

]
