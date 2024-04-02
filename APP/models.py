# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import *

# from django.db import models

# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.FloatField()
#     expiry_date = models.DateField()
#     quantity = models.IntegerField()

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     contact = models.CharField(max_length=20)
#     password = models.CharField(max_length=255)
#     email = models.EmailField()

# class Cart(models.Model):
#     cart_cookie_id = models.AutoField(primary_key=True)
#     total_amount = models.FloatField()

# class Orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_amount = models.FloatField()
#     delivery_by_date = models.DateField()
#     status = models.CharField(max_length=255)
#     payment_details = models.TextField()
#     transaction_id = models.CharField(max_length=255)
#     coupon_id = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True)

# class Coupon(models.Model):
#     coupon_id = models.AutoField(primary_key=True)
#     amount = models.FloatField()
#     coupon_name = models.CharField(default="abc", max_length=25)

from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = [
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
]

CATEGORY_CHOICES=[
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
]
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name



class Cart(models. Model):
    user = models. ForeignKey (User, on_delete=models.CASCADE)
    product = models. ForeignKey (Product, on_delete=models.CASCADE)
    quantity = models. PositiveIntegerField(default=1)

@property
def total_cost(self):
    return self.quantity * self.product.discounted_price
