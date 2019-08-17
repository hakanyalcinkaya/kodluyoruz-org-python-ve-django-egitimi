from django.contrib import admin
from .models import ShoppingCart, ShoppingCartItem

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)