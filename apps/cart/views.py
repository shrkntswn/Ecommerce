from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from products.models import Product
 

def cart(request):
    carts = Cart.objects.filter(user=request.user).order_by('-id')
    def sub_total_price():
        sub_total_price = 0
        for item in carts:
            sub_total_price = sub_total_price + item.totalprod_price()
        return sub_total_price
    if sub_total_price()  >= 500.0:
        shipping_charge = 0
    else:
        shipping_charge = 50.0
    context = {'carts':carts, 'sub_total_price': sub_total_price(),'tprice':sub_total_price()+shipping_charge, 'shipping_charge':shipping_charge}
    return render(request, 'cart/cart.html', context)

def addtocart(request, prod_id, id):
    product = Product.objects.get(prod_id=prod_id, id=id)
    carts = Cart.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        if product.prod_id not in [_.product.prod_id for _ in carts]:
            cart = Cart.objects.create(user=request.user, product=product)
        else:
            return redirect('cart:qtyInc', prod_id, id)
    return redirect('cart:cart')

def deleteItemCart(request, id):
    #product = Product.objects.get(id=id)
    cart = Cart.objects.get(id=id)
    if request.method == 'POST':
        cart.delete()
    return redirect('cart:cart')

def qtyInc(request, prod_id, id):
    print(prod_id)
    cart = get_object_or_404(Cart, product__prod_id=prod_id, product__id=id, user=request.user)
    print(cart)
    print(id)
    cart.quantity += 1
    cart.save()
    return redirect('cart:cart')

def qtyDec(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)
    cart.quantity -= 1
    cart.save()
    if cart.quantity == 0:
        cart.delete()
    return redirect('cart:cart')

def qty(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)
    qty = request.POST.get('quantity')
    try:
        if int(qty) == 0:
            cart.delete()
        if qty > 0:
            cart.quantity = qty
            cart.save()
    except:
        return redirect('cart:cart')
    return redirect('cart:cart')

