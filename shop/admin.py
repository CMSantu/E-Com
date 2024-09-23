from django.contrib import admin
from shop.models import Product,Order,OrderItem,Category

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)

# Register your models here.
