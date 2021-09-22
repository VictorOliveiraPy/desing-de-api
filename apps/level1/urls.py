from django.urls import path
from . import api

urlpatterns = [
    path('order/create', api.barista),
]
