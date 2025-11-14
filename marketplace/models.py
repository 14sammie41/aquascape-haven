from django.db import models

class Product(models.Model):
    """
    Model representing a product in the marketplace.
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
    
    @property
    def display_price(self):
        return self.price
