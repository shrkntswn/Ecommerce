from django.urls import path
from . import views

app_name='eshop_proj'
urlpatterns = [
    path('login/', views.userLogin, name='login'), 
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.acc_register, name='register'),
]