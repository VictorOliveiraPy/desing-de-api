from django.urls import path
from . import api

urlpatterns = [
    path('PlaceOrder', api.barista),
]
