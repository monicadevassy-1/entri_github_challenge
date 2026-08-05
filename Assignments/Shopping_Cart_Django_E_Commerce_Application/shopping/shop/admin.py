from django.contrib import admin

# Register your models here.
from .models import Category, Product, Cart, CartItem,Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Profile)