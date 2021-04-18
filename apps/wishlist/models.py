from django.db import models
from products.models import Product 

class Wishlist(models.Model):
    item = models.ForeignKey(Product, on_delete= models.CASCADE)
    def __str__(self):
        return self.id
