from django.contrib import admin

# Register your models here.
from Store.models import Category,Product,cart
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(cart)



