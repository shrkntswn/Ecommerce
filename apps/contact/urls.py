from django.urls import path
from . import views

app_name = 'eshop_proj'
urlpatterns = [
    path('contact/', views.contact, name='contactus'),
]