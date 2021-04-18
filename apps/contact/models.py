from django.db import models
import datetime

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default="False", blank=True, null=True)

    def __str__(self):
        return self.email


