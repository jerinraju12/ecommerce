from django.db import models

# Create your models here.
from jshop_app.models import Product


class Cartlist(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class Items(models.Model):
    prodt = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prodt
