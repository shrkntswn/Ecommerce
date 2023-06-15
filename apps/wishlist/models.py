from django.db import models
from products.models import Product 
from django.contrib.auth.models import User

class Wishlist(models.Model):
    wishlistitem = models.ForeignKey(Product, on_delete= models.CASCADE)
    user= models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.id
