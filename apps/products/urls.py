from django.urls import path
from . import views

app_name = 'eshop_proj'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/pid=<str:prod_id>/', views.productDetails, name='productDetails'),
    path('shop/<int:id>/', views.shop, name='shop')
]