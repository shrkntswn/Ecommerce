from django.db import models
from django.contrib.auth.models import User

class PrimaryAddress(models.Model):
    name = models.CharField(max_length = 100, blank=True, null=True)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True,null=True)
    area = models.CharField(max_length=50,)
    region = models.CharField(max_length=50,)
    country = models.CharField(max_length=50,)
    pin = models.PositiveIntegerField()
    def __int__(self):
        self.id

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.ImageField(blank=True, null=True)
    phone_num = models.PositiveIntegerField(blank=True, null=True)
    address_p = models.OneToOneField(PrimaryAddress, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        self.user.username




    

