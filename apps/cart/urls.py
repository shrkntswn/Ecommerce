from django.urls import path
from . import views

app_name = 'eshop_proj'
urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('add-to-cart/<str:id>', views.addtocart, name="addtocart"),
    path('delete/<int:id>', views.deleteItemCart, name="deleteItem"),
    path('inc/<int:id>', views.qtyInc, name="qtyInc"),
    path('dec/<int:id>', views.qtyDec, name="qtyDec"),
    path('qty/<int:id>', views.qty, name="qty"),
]