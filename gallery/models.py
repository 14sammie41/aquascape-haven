from django.db import models

class Aquascape(models.Model):
    """
    Model representing an aquascape entry in the gallery.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='aquascapes/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
