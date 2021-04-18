from django.db import models
import datetime
from django.utils.text import slugify

class CarouselImage(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/carousel_img', blank=True, null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True, blank=True, null=True)
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = 'categories'

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=True, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    sub_cat_image = models.ImageField(upload_to='products/sub-category-image', blank=True, null=True) 
    def __str__(self):
        return self.sub_category + '-' + self.category.category
    class Meta:
        verbose_name_plural = 'sub categories'

class Brand(models.Model):
    brand = models.CharField(max_length=100, unique=True)
    enable = models.BooleanField(default=True)
    def __str__(self):
        return self.brand

class Product(models.Model):
    prod_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    title = models.CharField(max_length=100)
    s_desc = models.CharField(max_length=100, null=True, blank=True)
    l_desc = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete= models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, blank=True, null=True)
    colours = models.CharField(max_length=50, blank=True, null=True)
    mrp = models.FloatField(null=True, blank=True)
    sell_price =models.FloatField(null=True, blank=True)
    released_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    enable = models.BooleanField(default=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.prod_id + '-' + self.title

    def save(self, *args, **kwargs):
        #self.prod_id = self.prod_id + str(self.id)
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Products'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/product_sub_images')
    def __str__(self):
        return str(self.product.prod_id) +'-'+str(self.id)

class FeatureItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.item.title + '-' + self.item.prod_id
    