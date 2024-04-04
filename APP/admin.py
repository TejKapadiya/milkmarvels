# from django.contrib import admin
# from .models import Product, User, Cart, Orders, Coupon

# # Register your models here.

# admin.site.register(Product)
# admin.site.register(User)
# admin.site.register(Cart)
# admin.site.register(Orders)
# admin.site.register(Coupon)

# # Register your models here.

from django.contrib import admin
from .models import Product ,Customer, Cart,Payment,OrderPlaced

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'category', 'product_image']
    # search_fields = ('title', 'description', 'composition')
    
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'locality', 'city', 'zipcode', 'state']




@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Cart)
def delete_entry_with_zero_quantity(sender, instance, **kwargs):
    if instance.quantity == 0:
        instance.delete()

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'order_id', 'payment_status', 'payment_id', 'paid']
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']