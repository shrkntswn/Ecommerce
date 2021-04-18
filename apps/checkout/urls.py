from django.urls import path
from . views import *

app_name='eshop_proj'
urlspatterns = [
    path('payment/', views.payment, name='payment')
]