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
from .models import Product ,Customer

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'category', 'product_image']
    # search_fields = ('title', 'description', 'composition')
    
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'locality', 'city', 'zipcode', 'state']

