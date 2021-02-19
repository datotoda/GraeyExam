# from django.contrib.auth.views import LoginView
from django.urls import path

from ecommerce.views import make_order

app_name = 'ecommerce'

urlpatterns = [
    path('', make_order , name='make_order'),
]
