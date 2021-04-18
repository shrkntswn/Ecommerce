from django.shortcuts import render
from .models import *

def wishlist(request):
    products = Wishlist.objects.all().order_by('-id')
    print(products[0].item.main_image)
    context={'products':products}
    return render(request, 'wishlist/wishlist.html', context)

def removeFromList(request):
    return None
