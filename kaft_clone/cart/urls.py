from django.urls import path
from .views import (
    shopping_cart_item_add
)


urlpatterns = [
    path('add/<int:cart_item_id>/', shopping_cart_item_add, name='shopping_cart_item_add'),  
] 
