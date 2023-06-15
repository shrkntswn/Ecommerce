from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def viewwishlist(request):
    #products = Wishlist.objects.all().order_by('-id')
    #print(products[0].item.main_image)
    products=Wishlist.objects.filter(user=request.user).order_by('id')
    context={'products':products}
    return render(request, 'wishlist/wishlist.html', context)

def addtowishlist(request, id):
    product=get_object_or_404(Product, id=id)


def removeFromList(request):
    return None

############################################

"""def addtocart(request, id):
    product = Product.objects.get(id=id)
    carts = Cart.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        if product.prod_id not in [_.product.prod_id for _ in carts]:
            cart = Cart.objects.create(user=request.user, product=product)
        else:
            return redirect('cart:qtyInc', id)
    return redirect('cart:cart')

def deleteItemCart(request, id):
    #product = Product.objects.get(id=id)
    cart = Cart.objects.get(id=id)
    if request.method == 'POST':
        cart.delete()
    return redirect('cart:cart')"""