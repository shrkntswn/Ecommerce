from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.prod_id

    def totalprod_price(self):
        price = self.product.sell_price * self.quantity
        return price
