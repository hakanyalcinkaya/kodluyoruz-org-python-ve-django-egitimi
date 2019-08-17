from django.db import models
from product.models import Product
from django.contrib.auth.models import User

STATUS = [
    # left side: DB
    # right side: human-readable name
    ('waiting', 'Bekleniyor'),
    ('buyed', 'Satinalindi'),
    ('deleted', 'Silindi'),
]


class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    is_deleted = models.BooleanField(default=False)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    items = models.ManyToManyField(ShoppingCartItem, blank=True)
    total_price = models.FloatField()
    status = models.CharField(
        default="waiting", 
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)