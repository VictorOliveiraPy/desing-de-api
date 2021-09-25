from django.urls import path

from . import api

urlpatterns = [
    path('order/create', api.create),
    path('order/delete', api.delete),

]
