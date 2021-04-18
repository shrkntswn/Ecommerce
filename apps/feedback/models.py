from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    
    def __str__(self):
        return self.user.usernme + self.product.prod_id
