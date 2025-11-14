from django.db import models
from marketplace.models import Product

class BasketItem(models.Model):
    """
    Model to represent an item in the shopping basket.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
