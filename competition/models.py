from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='competition_entries/')
    description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    is_winner = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
