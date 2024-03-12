from django.db import models

# Create your models here.
from django.contrib.auth.models import *

from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    email = models.EmailField()

class Cart(models.Model):
    cart_cookie_id = models.AutoField(primary_key=True)
    total_amount = models.FloatField()

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    delivery_by_date = models.DateField()
    status = models.CharField(max_length=255)
    payment_details = models.TextField()
    transaction_id = models.CharField(max_length=255)
    coupon_id = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True)

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    coupon_name = models.CharField(default="abc", max_length=25)