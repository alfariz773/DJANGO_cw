from django.db import models
# Create your models here.
class moviefan(models.Model):
    movie = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.movie} ({self.year})"
    