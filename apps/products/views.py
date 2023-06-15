from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Sidebar components
class Sidebar():
    categories = Category.objects.all()
    brands = Brand.objects.filter(enable=True).order_by('-id')


def index(request, *args, **kwargs):
    carouselimgs = CarouselImage.objects.all().order_by('-id')
    categories = Sidebar.categories
    brands = Sidebar.brands
    new_products = Product.objects.all().order_by('-id')
    # for products in new arrival carousel 
    def prodlist():
        new_list = []
        new_final = []
        for prod in new_products:
            new_list.append(prod)
            if len(new_list) == 3: # 3 items in each slider
                new_final.append(new_list)
                new_list=[]
        return new_final 
    featureItems = FeatureItem.objects.all().order_by('-id')
    context={'carouselimgs':carouselimgs,'featureItems':featureItems, 'categories':categories, 'brands':brands, 'new_products':new_products,'prodlist':prodlist()}
    return render(request, 'products/index.html', context)

def productDetails(request, slug, prod_id):
    categories = Sidebar.categories
    brands = Sidebar.brands
    featureItems = FeatureItem.objects.all()
    product = get_object_or_404(Product, prod_id=prod_id)
    context={"product":product,'featureItems':featureItems, 'categories':categories, 'brands':brands}
    return render(request, 'products/product-details.html', context)

    
def shop(request, id):
    categories = Sidebar.categories
    sub_cat_obj = get_object_or_404(SubCategory, id=id)
    products = Product.objects.filter(sub_category__id = id)
    try:
        max_value = 10**int(len(str(int(max([product.sell_price for product in products])))))
    except:
        max_value = 0
    selected_value_min=0
    selected_value_max=max_value
    if request.method == "POST":
        try:
            slider = request.POST.get('slider')
            slider_list = [x for x in slider.split(',')]
            selected_value_min=slider_list[0]
            selected_value_max=slider_list[1]
            products = Product.objects.filter(sub_category__id = id, sell_price__range = (slider_list[0], slider_list[1]))
        except:
            products = Product.objects.filter(sub_category__id = id)

    print('slider',selected_value_min)   
    items = sub_cat_obj.product_set.all()
    brands_list =[]
    price_slider = True
    for item in items:
        brands_list.append(item.brand)
    brands = tuple(brands_list)
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 15)
    try:
        pg = paginator.page(page)
    except PageNotAnInteger:
        pg = paginator.page(1)
    except EmptyPage:
        pg = paginator.page(paginator.num_pages)
    products_after_pagiation = pg
    context = {'max_value':max_value, 'price_slider':price_slider, 'categories':categories, 'brands':brands, 'sub_cat_obj':sub_cat_obj, 'products':products_after_pagiation, 'page':pg, 'selected_value_min':selected_value_min, 'selected_value_max':selected_value_max}
    return render(request, 'products/shop.html', context)

